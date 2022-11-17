# -------------------------------------------
# JADE
# Ana Lizbeth Zermeño Torres     A00824913
# Ana Carolina Arellano Alvarez  A01650945
# November 2022
# ------------------------------------------

# Import Lex and Yacc
from asyncio import create_subprocess_exec
from queue import Empty
from quadrupleFunctions import validateOperator
from stack import Stack
from tkinter.tix import TCL_DONT_WAIT
import ply.lex as lex
from ply.yacc import yacc
from functionDirectory import FunctionDirectory
from semanticCube import CUBE
from virtualMachine import virtualMachine
from stack import Stack
from virtualMemory import Memory
import quadruples

operatorStack = Stack()
operandStack = Stack()
jumpsStack = Stack()
typeStack = Stack()

operatorStack.add('end')
quadrupleList = []

id = 0
param = 0
idTemp = 0

# Tokens
reserved = {
    'program': 'PROGRAM',
    'class': 'CLASS',
    'var': 'VAR',
    'assign': 'ASSIGN',
    'fun': 'FUN',
    'return': 'RETURN',
    'int': 'INT',
    'float': 'FLOAT',
    'bool': 'BOOL',
    'mod': 'MOD',
    'main': 'MAIN',
    'void': 'VOID',
    'if': 'IF',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'in': 'IN',
    'or': 'OR',
    'and': 'AND',
    'read': 'READ',
    'print': 'PRINT',
    'for': 'FOR',
    'while': 'WHILE',
    'return': 'RETURN'
}

# Token declaration
tokens = [
    'SEMICOLON',
    'COLON',
    'COMMA',
    'DOT',
    'PLUS',
    'MINUS',
    'MULT',
    'DIV',
    'OPARENTHESIS',
    'CPARENTHESIS',
    'OBRACKET',
    'CBRACKET',
    'OCURLY',
    'CCURLY',
    'LESSTHAN',
    'GREATERTHAN',
    'NOTEQUAL',
    'ISEQUAL',
    'EQUAL',
    'ID',
    'CLASSID',
    'OBJID',
    'CTEINT',
    'CTEFLOAT',
    'CTESTRING',
    'COMMENT'
] + list(reserved.values())

# Ignore
t_ignore = ' \t'

# Token matching
t_SEMICOLON = r'\;'
t_COLON = r'\:'
t_COMMA = r'\,'
t_DOT = r'\.'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_OPARENTHESIS = r'\('
t_CPARENTHESIS = r'\)'
t_OBRACKET = r'\['
t_CBRACKET = r'\]'
t_OCURLY = r'\{'
t_CCURLY = r'\}'
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_EQUAL = r'\='
t_NOTEQUAL = r'\!='
t_ISEQUAL = r'\=='


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_CLASSID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_COBJID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_CTEFLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_CTEINT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_CTESTRING(t):
    r'"^[a-zA-Z0-9_]+( [a-zA-Z0-9_]+)*$"'
    t.value = str(t.value)
    return t


# Ignore comments
t_ignore_COMMENT = r'\//.*'

# Ignored token with an action associated with it


def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# Error handler for illegal characters


def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)
    global dError
    dError = False


# Build the lexer object
lexer = lex.lex()

# Parser
# Functions for each grammar rule

def p_program(p):
    '''
    program : PROGRAM createDir OCURLY block main CCURLY
    '''

def p_createDir(p):
    '''
    createDir : ID
    '''
    # Create global directory
    global programDirectory
    programDirectory = FunctionDirectory()
    programDirectory.setId("program")
    programDirectory.addFunction(programDirectory.returnId(), "program", 0)
    programDirectory.addFunction("local", "local", 0)
    global scopeList
    scopeList = []
    scopeList.append(programDirectory.returnId())

def p_main(p):
    '''
    main : MAIN mainScope OCURLY block4 CCURLY 
    '''

def p_mainScope(p):
    '''
    mainScope : 
    '''
    scopeList.append("local")
    programDirectory.setType("main")

def p_block(p):
    '''
    block : block2 block3 block4
    '''

def p_block2(p):
    '''
    block2 : var block2
           | empty
    '''

def p_block3(p):
    '''
    block3 : fun block3
           | empty
    '''

def p_block4(p):
    '''
    block4 : statement block4
           | empty
    '''

def p_statement(p):
    '''
    statement : assign
              | write
              | read
              | condition
              | forloop
              | whileloop
              | funcall
              | class
    '''

def p_var(p):
    '''
    var : VAR INT ID endOfExp
        | VAR FLOAT ID endOfExp
        | VAR BOOL ID endOfExp
    '''
    currScope = scopeList[len(scopeList)-1]
    vardir = Memory.assignDir(currScope, p[2])
    name = p[3]
    if currScope == "program" or currScope == "local":
        programDirectory.getVarTable().addVar(name, p[2], 0, currScope, vardir)
# def p_var3( p ):
#    '''
#    var3 : setVar var2
#         | OBRACKET varArray CBRACKET COMMA var2
#         | setVar2
#    '''

def p_varArray(p):
    '''
    varArray : CTEINT
    '''
    size = p[1]
    programDirectory.getVarTable().addVar(programDirectory.returnId(),
                                          programDirectory.returnType(), size, 0)

def p_type(p):
    '''
    type : INT
         | FLOAT
         | BOOL
    '''
    if p[1] != None and p[-1] == 'var':
        typeStack.add(p[1])

    programDirectory.setType(p[1])

def p_assign(p):
    '''
    assign : ASSIGN assign2 endOfExp
    '''

def p_assign2(p):
    '''
    assign2 : ID EQUAL opadd addOperand 
    '''
    if programDirectory.getVarTable().idExist(p[1]):
        operandStack.add(p[1])
        typeStack.add(
            programDirectory.getVarTable().getItem(p[1]).returnType())
    else:
        print("Error: La variable no ha sido declarada antes de su uso")

def p_condition(p):
    '''
    condition : IF condition2 end
    '''

def p_condition2(p):
    '''
    condition2 : OPARENTHESIS expression CPARENTHESIS gotoF OCURLY block CCURLY condition3
    '''

def p_condition3(p):
    '''
    condition3 : ELSEIF condition2
               | ELSE goto OCURLY block CCURLY
               | empty
    '''

def p_write(p):
    '''
    write : PRINT OPARENTHESIS write2 CPARENTHESIS endOfExp
    '''

def p_write2(p):
    '''
    write2 : expression printparam write3
           | CTESTRING printstring write3
    '''

def p_write3(p):
    '''
    write3 : COMMA write2
           | empty
    '''

def p_printparam(p):
    '''
    printparam :
    '''
    printQuadruple()

def p_printstring(p):
    '''
    printstring :
    '''
    global id
    tempQuad = quadruples.Quadruple(id, 'print', '', '', p[-1])
    quadrupleList.append(tempQuad)
    id += 1

def p_read(p):
    '''
    read : READ ID endOfExp
    '''

def p_fun(p):
    ''' 
    fun : FUN fun_addFun OPARENTHESIS funparams CPARENTHESIS OCURLY block CCURLY endfun
    '''

def p_fun_addFun(p):
    '''
    fun_addFun : type ID
               | VOID ID
    '''
    programDirectory.setType(p[1])
    scopeList.append("local")

def p_funcall(p):
    ''' 
    funcall : ID era OPARENTHESIS funcall2 CPARENTHESIS SEMICOLON gosub
    '''

def p_funcall2(p):
    ''' 
    funcall2 : params
             | empty
    '''

def p_forloop(p):
    '''
    forloop : FOR OPARENTHESIS for_id EQUAL expression for_endexpid COLON expression for_endexpcond CPARENTHESIS OCURLY statement CCURLY for_end
    '''

def p_expression(p):
    '''
    expression : t_exp expression2
    '''
    endOfExpresion()

def p_expression2(p):
    '''
    expression2 : OR opadd expression
                | empty
    '''


def p_t_exp(p):
    '''
    t_exp : g_exp t_exp2
    '''

def p_t_exp2(p):
    '''
    t_exp2 : AND opadd t_exp
           | empty
    '''

def p_g_exp(p):
    '''
    g_exp : m_exp g_exp2
    '''

def p_g_exp2(p):
    '''
    g_exp2 : GREATERTHAN opadd m_exp
           | LESSTHAN opadd m_exp
           | ISEQUAL opadd m_exp
           | NOTEQUAL opadd m_exp
           | empty
    '''

def p_m_exp(p):
    '''
    m_exp : t m_exp2
    '''

def p_m_exp2(p):
    '''
    m_exp2 : PLUS opadd m_exp
           | MINUS opadd m_exp
           | empty
    '''

def p_t(p):
    '''
    t : f t2
    '''

def p_t2(p):
    '''
    t2 : MULT opadd t
       | DIV opadd t
       | empty
    '''

def p_f(p):
    '''
    f : addFBottom expression popFBottom
      | addOperand
    '''

def p_endOfExp(p):
    '''
    endOfExp : SEMICOLON
    '''
    endOfExpresion()

def p_addOperand(p):
    '''
    addOperand : varvalue
               | ID
    '''
    if p[1] != None:
        if programDirectory.getVarTable().idExist(p[1]):
            operandStack.add(p[1])
            typeStack.add(
                programDirectory.getVarTable().getItem(p[1]).returnType())
        else:
            print("Error: La variable no ha sido declarada antes de su uso")

def p_opadd(p):
    '''
    opadd :
    '''
    if operandStack.size() > 0:
        if validateOperator(p[-1], operatorStack.top()):
            createQuadruple()
    operatorStack.add(p[-1])

def p_addFBottom(p):
    '''
    addFBottom : OPARENTHESIS
    '''
    operatorStack.addFakeBottom()

def p_popFBottom(p):
    '''
    popFBottom : CPARENTHESIS
    '''
    operatorStack.popFakeBottom()

def p_params(p):
    '''
    params : ID addparam params2
           | CTEINT addparam params2
           | CTEFLOAT addparam params2
           | empty
    '''

def p_params2(p):
    '''
    params2 : COMMA params
            | empty
    '''

def p_funparams(p):
    '''
    funparams : type ID  funparams2
              | empty
    '''

def p_funparams2(p):
    '''
    funparams2 : COMMA funparams
            | empty
    '''

def p_whileloop(p):
    '''
    whileloop : WHILE whilepoint g_exp CPARENTHESIS gotoF OCURLY block CCURLY whileend
    '''

def p_varvalue(p):
    '''
    varvalue : CTEINT
             | CTEFLOAT
             | CTESTRING
    '''
    if programDirectory.getVarTable().idExist(p[-3]):
        itemType = programDirectory.getVarTable().getItem(p[-3]).returnType()
        myType = str(type(p[1]))
        newType = myType[8:11]
        if itemType == newType:
            operandStack.add(p[1])
            typeStack.add(itemType)
        elif myType[8:12] == newType:
            operandStack.add(p[1])
            typeStack.add(itemType)
        else:
            print("Error: el tipo de variable no coincide con el valor asignado ")

def p_class(p):
    '''
    class : CLASS ID OCURLY class2 class3 CCURLY
    '''

def p_class2(p):
    '''
    class2 : attribute class2
            | empty
    '''

def p_class3(p):
    '''
    class3 : method class3
           | empty
    '''

def p_obj_constructor(p):
    '''
    obj_constructor : CLASSID ID OPARENTHESIS params CPARENTHESIS OCURLY block CCURLY
    '''

def p_obj_declaration(p):
    '''
    obj_declaration : CLASSID OBJID OPARENTHESIS params CPARENTHESIS endOfExp
    '''

def p_obj_method_access(p):
    '''
    obj_method_access : OBJID DOT method endOfExp
    '''

def p_obj_attr_access(p):
    '''
    obj_attr_access : OBJID DOT attribute endOfExp
    '''

def p_method(p):
    '''
    method : fun
    '''

def p_attribute(p):
    '''
    attribute : var
    '''

def p_return(p):
    '''
    return : RETURN ID endOfExp
    '''

def p_empty(p):
    '''
    empty : 
    '''
    pass

def p_end(p):
    '''
    end : 
    '''
    end = jumpsStack.pop()
    fill(end, id)

##################################
#             MODULES            #
##################################

def p_era(p):
    '''
    era : 
    '''
    global id
    tempQuad = quadruples.Quadruple(id, 'ERA', '', '', '')
    tempQuad.setResult(p[-1])
    quadrupleList.append(tempQuad)
    id += 1

def p_gosub(p):
    '''
    gosub : 
    '''
    global id
    tempQuad = quadruples.Quadruple(id, 'GOSUB', '', '', '')
    tempQuad.setResult(p[-6])  # Cambiar por direccion
    global scopeList
    scopeList.append(p[-6])
    quadrupleList.append(tempQuad)
    id += 1

def p_addparam(p):
    '''
    addparam : 
    '''
    global id
    tempQuad = quadruples.Quadruple(id, 'PARAM', '', '', '')
    if programDirectory.getVarTable().idExist(p[-1]):
        operandStack.add(p[-1])
        typeStack.add(
            programDirectory.getVarTable().getItem(p[-1]).returnType())
    else:
        print("Error en parámetros")

    tempQuad.setOperandLeft(operandStack)
    operandStack.pop()
    tempQuad.setResult(createParamTemp())
    quadrupleList.append(tempQuad)
    id += 1

def p_endfun(p):
    '''
    endfun : 
    '''
    global id
    tempQuad = quadruples.Quadruple(id, 'ENDFUN', '', '', '')
    quadrupleList.append(tempQuad)
    id += 1

##################################
#              WHILE             #
##################################
def p_whilepoint(p):
    '''
    whilepoint : OPARENTHESIS
    '''
    jumpsStack.add(id)

def p_whileend(p):
    '''
    whileend : 
    '''
    global id
    end = jumpsStack.pop()
    whileReturn = jumpsStack.pop()
    tempQuad = quadruples.Quadruple(id, 'goto', '', '', '')
    tempQuad.setResult(whileReturn)
    quadrupleList.append(tempQuad)
    id += 1
    fill(end, id)

##################################
#              FOR               #
##################################

def p_for_id(p):
    '''
    for_id : ID
    '''
    if programDirectory.getVarTable().idExist(p[1]):
        operandStack.add(p[1])
        typeStack.add(
            programDirectory.getVarTable().getItem(p[1]).returnType())
    else:
        print("Error: No se ha declarado la variable contadora")

def p_for_endexpid(p):
    '''
    for_endexpid : 
    '''
    #expType = typeStack.pop()
    # if expType != "int":   validar que exp_type sea numerico
    #   print("error")
    global id
    exp = operandStack.pop()
    global vcontrol
    vcontrol = operandStack.top()
    # controlType = typeStack.pop()
    # typeRes = checktype(=,controlType,expType)
    tempQuad = quadruples.Quadruple(id, '=', exp, '', vcontrol)
    quadrupleList.append(tempQuad)
    id += 1

def p_for_endexpcond(p):
    '''
    for_endexpcond : 
    '''
    global id
    global vcontrol
    #expType = typeStack.pop()
    exp = operandStack.pop()
    vfinal = 'vfinal'
    tempQuad = quadruples.Quadruple(id, '=', exp, '', vfinal)
    quadrupleList.append(tempQuad)
    id += 1
    tempQuad = quadruples.Quadruple(id, '<', vcontrol, vfinal, '')
    tempOperand = createTemp()
    operandStack.add(tempOperand)
    tempQuad.setResult(tempOperand)
    quadrupleList.append(tempQuad)
    id += 1
    jumpsStack.add(id-1)
    gotoFQuadruple()

def p_for_end(p):
    '''
    for_end : 
    '''
    global id
    global vcontrol
    tempQuad = quadruples.Quadruple(id, '+', vcontrol, 1, '')
    ty = createTemp()
    tempQuad.setResult(ty)
    quadrupleList.append(tempQuad)
    id += 1
    tempQuad = quadruples.Quadruple(id, '=', ty, '', vcontrol)
    quadrupleList.append(tempQuad)
    id += 1
    #tempQuad = quadruples.Quadruple(id,'=',ty,'',operandStack.top())
    # quadrupleList.append(tempQuad)
    #id += 1
    fin = jumpsStack.pop()
    ret = jumpsStack.pop()
    tempQuad = quadruples.Quadruple(id, 'goto', '', '', ret)
    quadrupleList.append(tempQuad)
    id += 1
    fill(fin, id)
    operandStack.pop()
    #typDelete = typestack.pop()

# Error handler for illegal syntaxis
def p_error(p):
    print("Syntax error at " + str(p.value))
    global dError
    dError = False

##################################
#   CREATE QUADRUPLE FUNCTIONS   #
##################################

def createQuadruple():
    if operatorStack.top() == '=':
        assignQuadruple()
    else:
        operationQuadruple()

def createTemp():
    global idTemp
    idTemp += 1
    myTemp = "temp" + str(idTemp)
    currScope = scopeList[len(scopeList)-1]
    # cambiar para enviar verdadero tipo
    vardir = Memory.assignDir(currScope, "int")
    programDirectory.getVarTable().addVar(myTemp, "int", 0, currScope, vardir)
    return myTemp

def createParamTemp():
    global param
    param += 1
    myTemp = "param" + str(param)
    return myTemp

def assignQuadruple():
    global id
    tempQuad = quadruples.Quadruple(id, '', '', '', '')
    tempQuad.setValues(operandStack, operatorStack)
    quadrupleList.append(tempQuad)
    id += 1

def operationQuadruple():
    global id
    tempQuad = quadruples.Quadruple(id, '', '', '', '')
    opL = operandStack.pop()
    opR = operandStack.top()
    # print(CUBE["int"]["int"][operatorStack.top()])
    operandStack.add(opL)
    tempQuad.setValues(operandStack, operatorStack)
    tempOperand = createTemp()
    operandStack.add(tempOperand)
    tempQuad.setResult(tempOperand)
    quadrupleList.append(tempQuad)
    id += 1

def printQuadruple():
    global id
    tempQuad = quadruples.Quadruple(id, 'print', '', '', '')
    tempQuad.setResult(operandStack.top())
    operandStack.pop()
    quadrupleList.append(tempQuad)
    id += 1

def gotoFQuadruple():
    # Aqui va la validacion de tipo, si es bool genera cuadruplo
    global id
    tempQuad = quadruples.Quadruple(id, 'gotoF', '', '', '')
    tempQuad.setOperandLeft(operandStack)
    operandStack.pop()
    quadrupleList.append(tempQuad)
    jumpsStack.add(id)
    id += 1

def endOfExpresion():
    if operatorStack.size() == 1:
        if operatorStack.top() == "print":
            printQuadruple()
        elif operatorStack.top() == '=':
            assignQuadruple()
    else:
        while operandStack.size() > 1 and operatorStack.size() > 1:
            operationQuadruple()

def fill(top, id):
    for item in quadrupleList:
        if item.id == top:
            item.setResult(id)

##################################
#       GOTO, GOTOF, GOTOT       #
##################################
def p_gotoF(p):
    '''
    gotoF :
    '''
    gotoFQuadruple()


def p_goto(p):
    '''
    goto :
    '''
    global id
    tempQuad = quadruples.Quadruple(id, 'goto', '', '', '')
    quadrupleList.append(tempQuad)
    false = jumpsStack.pop()
    jumpsStack.add(id)
    id += 1
    fill(false, id)

# Build the parser
parser = yacc()
dError = True
print("*Test case - correct")
text = '''
program test1 {
    var float num;
    var int prueba1;

    var int i;

    fun void funcion(){
        var float num2;
    }

    assign i = 0;
    main {
        function(num2);
        print(num + num2);
        print(prueba1 + num2);
    }

}'''
case_TestCorrect = parser.parse(text)

if (dError == True):
    # quadruples.printQuadrupleList(quadrupleList)
    print("INICIO MAQUINA VIRTUAL")
    maquinaVirtual = virtualMachine(
        programDirectory.returnDirectory(), quadrupleList)
    maquinaVirtual.virtualMachineStart()
else:
    print("Failed")

dError = True
