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
funIds = []
quadrupleList = []
eraData = []

id = 0
param = 0
idTemp = 0

# Tokens
reserved = {
    'program': 'PROGRAM',
    'class': 'CLASS',
    'var': 'VAR',
    'array': 'ARRAY',
    'matrix': 'MATRIX',
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
    'LESSOREQUAL',
    'GREATEROREQUAL',
    'ID',
    'CLASSID',
    'OBJID',
    'CTEINT',
    'CTEFLOAT',
    'CTESTRING',
    'COMMENT',
    'QUOTE'
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
t_LESSOREQUAL = r'\<='
t_GREATEROREQUAL = r'\>='
t_QUOTE = r'\"'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_CLASSID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'CLASSID')
    return t


def t_OBJID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'OBJID')
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
    r'^[a-zA-Z0-9_]+( [a-zA-Z0-9_]+)*$'
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
    program : PROGRAM createDir OCURLY block main CCURLY endprog
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
    global id
    tempQuad = quadruples.Quadruple(id, 'goto', '', '', '')
    quadrupleList.append(tempQuad)
    id += 1

def p_endprog(p):
    '''
    endprog :
    '''
    global id
    tempQuad = quadruples.Quadruple(id, 'endprog', '', '', '')
    quadrupleList.append(tempQuad)
    id += 1

def p_main(p):
    '''
    main : MAIN mainScope OCURLY block2 CCURLY 
    '''


def p_mainScope(p):
    '''
    mainScope : 
    '''
    scopeList.append("local")
    programDirectory.setType("main")
    quadrupleList[0].setResult(id)


def p_block(p):
    '''
    block : var block
          | varArray block
          | varMatrix block
          | fun block
          | statement block
          | empty
    '''


def p_block2(p):
    '''
    block2 : statement block2
           | var block2
           | varArray block2
           | varMatrix block2
           | empty
    '''


def p_statement(p):
    '''
    statement : assign
              | assignArray
              | assignMatrix
              | write
              | read
              | condition
              | forloop
              | whileloop
              | funcall
              | class
              | objdeclaration
              | objmethodaccess
              | objattraccess
              | var
    '''


def p_var(p):
    '''
    var : VAR INT ID endOfExp
        | VAR FLOAT ID endOfExp
        | VAR BOOL ID endOfExp
    '''
    currScope = scopeList[len(scopeList)-1]
    vardir = Memory.assignDir(currScope, p[2], 1)
    name = p[3]
    if currScope == "program" or currScope == "local":
        programDirectory.getVarTable().addVar(name, p[2], 1, currScope, vardir)


def p_varArray(p):
    '''
    varArray : VAR ARRAY INT ID EQUAL OBRACKET varArray2 CBRACKET SEMICOLON
            | VAR ARRAY FLOAT ID EQUAL OBRACKET varArray2 CBRACKET SEMICOLON
            | VAR ARRAY BOOL ID EQUAL OBRACKET varArray2 CBRACKET SEMICOLON
    '''


def p_varArray2(p):
    '''
    varArray2 : CTEINT
              | ID
    '''
    size = p[1]
    currScope = scopeList[len(scopeList)-1]
    vardir = Memory.assignDir(currScope, p[-4], size)
    programDirectory.getVarTable().addVar(p[-3],
                                          p[-4], size, currScope, vardir)


def p_varMatrix(p):
    '''
    varMatrix : VAR MATRIX INT ID EQUAL OBRACKET CTEINT CBRACKET OBRACKET CTEINT CBRACKET SEMICOLON
              | VAR MATRIX FLOAT ID EQUAL OBRACKET CTEINT CBRACKET OBRACKET CTEINT CBRACKET SEMICOLON
              | VAR MATRIX BOOL ID EQUAL OBRACKET CTEINT CBRACKET OBRACKET CTEINT CBRACKET SEMICOLON
    '''
    size = p[7] * p[10]
    currScope = scopeList[len(scopeList)-1]
    vardir = Memory.assignDir(currScope, p[3], size)
    programDirectory.getVarTable().addVar(p[4],
                                          p[3], size, currScope, vardir)


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
    assign : ASSIGN assign2 SEMICOLON
           | ASSIGN ID EQUAL ID OBRACKET ID CBRACKET SEMICOLON
           | ASSIGN ID EQUAL ID OBRACKET CTEINT CBRACKET SEMICOLON
    '''
    if p[2] != None:  # arreglo
        operatorStack.add("=")
        if programDirectory.getVarTable().idExist(p[2]) and programDirectory.getVarTable().idExist(p[4]):
            if str(type(p[6]))[8:11] != "int" and programDirectory.getVarTable().idExist(p[6]):  # pos is an ID
                typeStack.add(
                    programDirectory.getVarTable().getItem(p[4]).returnType())
                operandStack.add(p[4])
            elif str(type(p[6]))[8:11] == "int":  # pos is an integer
                typeStack.add(
                    programDirectory.getVarTable().getItem(p[4]).returnType())
                operandStack.add(p[4] + str(p[6]))
        else:
            print("Error: La variable no ha sido declarada antes de su uso")
            exit()
    assignQuadruple()


def p_assign2(p):
    '''
    assign2 : ID EQUAL assign3 
            | objattraccess EQUAL addOperand
    '''
    operatorStack.add("=")
    if p[1] != None:
        if programDirectory.getVarTable().idExist(p[1]):
            operandStack.add(p[1])
            typeStack.add(
                programDirectory.getVarTable().getItem(p[1]).returnType())
    else:
        print("Error: La variable no ha sido declarada antes de su uso")
        exit()


def p_assign3(p):
    '''
    assign3 : expression
            | addOperand
    '''


def p_assignArray(p):
    '''
    assignArray : ASSIGN ARRAY ID OBRACKET CTEINT CBRACKET EQUAL CTEINT SEMICOLON
                | ASSIGN ARRAY ID OBRACKET CTEINT CBRACKET EQUAL CTEFLOAT SEMICOLON
                | ASSIGN ARRAY ID OBRACKET CTEINT CBRACKET EQUAL BOOL SEMICOLON
                | ASSIGN ARRAY ID OBRACKET CTEINT CBRACKET EQUAL ID SEMICOLON
    '''
    # add quadruple to check bounds
    if not programDirectory.getVarTable().idExist(p[3]):
        print("Error, no se ha declarado el arreglo")
        exit()
    if p[5] < programDirectory.getVarTable().getItem(p[3]).returnSize() and p[5] >= 0:
        global id
        tempQuad = quadruples.Quadruple(
            id, 'VER', p[5], programDirectory.getVarTable().getItem(p[3]).returnSize(), p[3])
        quadrupleList.append(tempQuad)
        id += 1
    else:
        print("Error: índice fuera de los límites")
        exit()
    # Go to memory dir
    calc = programDirectory.getVarTable().getItem(p[3]).returnSize() - p[5]
    currScope = scopeList[len(scopeList)-1]
    currtype = programDirectory.getVarTable().getItem(p[3]).returnType()
    dir = programDirectory.getVarTable().getItem(p[3]).returnDir() - calc
    programDirectory.getVarTable().addVar(
        p[3]+str(p[5]), currtype, 1, currScope, dir)
    # Assign quadruple
    tempQuad = quadruples.Quadruple(id, p[7], p[3]+str(p[5]), '', p[8])
    quadrupleList.append(tempQuad)
    print(tempQuad.getOperator(), tempQuad.getOperandLeft(),
          tempQuad.getOperandRight(), tempQuad.getResult())
    id += 1


def p_assignMatrix(p):
    '''
    assignMatrix : ASSIGN MATRIX ID OBRACKET CTEINT CBRACKET OBRACKET CTEINT CBRACKET EQUAL expression SEMICOLON
    '''
    cell = p[5]*p[8]
    # check bounds
    if cell < programDirectory.getVarTable().getItem(p[3]).returnSize() and cell >= 0:
        global id
        tempQuad = quadruples.Quadruple(
            id, 'VER', p[5], programDirectory.getVarTable().getItem(p[3]).returnSize(), p[11])
        quadrupleList.append(tempQuad)
        id += 1
    else:
        print("Error: índice fuera de los límites")


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
           | ID OBRACKET CTEINT CBRACKET
           | ID OBRACKET ID CBRACKET  
    '''
    if (p[1] != None):  # print array cell
        global id
        tempQuad = quadruples.Quadruple(id, 'print', '', '', '')
        tempQuad.setResult(p[1]+str(p[3]))
        quadrupleList.append(tempQuad)
        id += 1


def p_write3(p):
    '''
    write3 : COMMA write2
           | empty
    '''


def p_printparam(p):
    '''
    printparam :
    '''
    endOfExpresion()
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
    fun : FUN fun_addFun OPARENTHESIS funparams CPARENTHESIS OCURLY block return CCURLY endfun
    '''


def p_fun_addFun(p):
    '''
    fun_addFun : type ID
               | VOID ID
    '''
    programDirectory.setType(p[1])
    scopeList.append("local")
    funIds.append([p[2], id])
    eraData.append([p[2], []])
    global currFun
    currFun = p[2]


def p_funcall(p):
    ''' 
    funcall : ID era OPARENTHESIS funcall2 CPARENTHESIS SEMICOLON gosub
    '''
    currFun = p[1]


def p_funcall2(p):
    ''' 
    funcall2 : params
             | empty
    '''


def p_forloop(p):
    '''
    forloop : FOR OPARENTHESIS for_id EQUAL expression for_endexpid COLON forcontrol for_endexpcond CPARENTHESIS OCURLY forstatements CCURLY for_end
    '''

def p_forstatements(p):
    '''
    forstatements : statement forstatements
                  | empty
    '''

def p_forcontrol(p):
    '''
    forcontrol : CTEINT
    '''
    operandStack.add(p[1])
    constdir = Memory.assignDir("constant", "constant", 1)
    programDirectory.getVarTable().addVar(p[1], "int", 1, "constant", constdir)


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
           | LESSOREQUAL opadd m_exp
           | GREATEROREQUAL opadd m_exp
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
            exit()


def p_opadd(p):
    '''
    opadd :
    '''
    if operandStack.size() > 0 and operatorStack.size() > 0:
        if validateOperator(p[-1], operatorStack.top()):
            createQuadruple()
        elif operatorStack.size() == 0:
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
    funparams : INT ID  
              | FLOAT ID  
              | BOOL ID
              | empty
    '''
    constdir = Memory.assignDir("local", p[1], 1)
    programDirectory.getVarTable().addVar(p[2], p[1], 1, "constant", constdir)
    for i in eraData:
        if i[0] == currFun:
            i[1].append(p[2])


def p_whileloop(p):
    '''
    whileloop : WHILE whilepoint g_exp endOfExp CPARENTHESIS gotoF OCURLY block CCURLY whileend
    '''


def p_varvalue(p):
    '''
    varvalue : CTEINT
             | CTEFLOAT
             | CTESTRING
    '''
    # Caso: asignación de variables assign num = 3 y num(id) es int
    if programDirectory.getVarTable().idExist(p[-3]):
        itemType = programDirectory.getVarTable().getItem(p[-3]).returnType()
        myType = str(type(p[1]))
        newType = myType[8:11]
        if itemType == newType:
            operandStack.add(p[1])
            typeStack.add(itemType)
        elif itemType == myType[8:13]:
            operandStack.add(p[1])
            typeStack.add(itemType)
        else:
            print("Error: el tipo de variable no coincide con el valor asignado ")
            exit()
    elif p[-4] == "for":
        operandStack.add(p[1])
        typeStack.add("int")
        constdir = Memory.assignDir("constant", "constant", 1)
        programDirectory.getVarTable().addVar(
            p[1], "int", 1, "constant", constdir)
    else:
        try:
            constdir = Memory.assignDir("constant", "constant", 1)
            if str(type(p[1]))[8:11] == "int":
                typeStack.add("int")
                programDirectory.getVarTable().addVar(
                    p[1], str(type(p[1]))[8:11], 1, "constant", constdir)
            elif str(type(p[1])[8:13]) == "float":
                typeStack.add("float")
                programDirectory.getVarTable().addVar(
                    p[1], str(type(p[1]))[8:13], 1, "constant", constdir)
            operandStack.add(p[1])
        except:
            operandStack.add(p[1])


def p_class(p):
    '''
    class : CLASS ID OCURLY class2 objconstructor class3 addclass CCURLY
    '''


def p_class2(p):
    '''
    class2 : var class2
           | empty
    '''


def p_class3(p):
    '''
    class3 : fun class3
           | empty
    '''


def p_addclass(p):
    '''
    addclass : empty
    '''
    # Agregar a directorio


def p_objconstructor(p):
    '''
    objconstructor : CLASSID OPARENTHESIS params CPARENTHESIS block
                   | empty
    '''


def p_objdeclaration(p):
    '''
    objdeclaration : CLASSID OBJID OPARENTHESIS params CPARENTHESIS endOfExp
    '''


def p_objmethodaccess(p):
    '''
    objmethodaccess : ID DOT ID era OPARENTHESIS funcall2 CPARENTHESIS SEMICOLON gosub
    '''
    operandStack.add(p[1] + '.' + p[3])


def p_objattraccess(p):
    '''
    objattraccess : ID DOT ID
    '''
    operandStack.add(p[1] + '.' + p[3])


def p_return(p):
    '''
    return : RETURN ID SEMICOLON
           | empty
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
    for item in funIds:
        if item[0] == p[-1]:
            tempQuad.setResult(item[1])
    tempQuad.setResult(p[-1])
    quadrupleList.append(tempQuad)
    id += 1


def p_gosub(p):
    '''
    gosub : 
    '''
    global id
    tempQuad = quadruples.Quadruple(id, 'GOSUB', '', '', '')
    found = False
    for item in funIds:
        if item[0] == p[-6]:
            tempQuad.setResult(item[1])
            found = not found
    if found == False:
        print("Error: la función aún no ha sido definida")
        exit()  # Cambiar por direccion
    global scopeList
    scopeList.append("local")
    quadrupleList.append(tempQuad)
    id += 1


def p_addparam(p):
    '''
    addparam : 
    '''
    global id
    tempQuad = quadruples.Quadruple(id, 'PARAM', '', '', '')
    if str(type(p[-1]))[8:11] == "int":
        operandStack.add(p[-1])
        typeStack.add("int")
        constdir = Memory.assignDir("constant", "constant", 1)
        programDirectory.getVarTable().addVar(
            p[-1], "int", 1, "constant", constdir)
    elif str(type(p[-1]))[8:13] == "float":
        operandStack.add(p[-1])
        typeStack.add("float")
        constdir = Memory.assignDir("constant", "constant", 1)
        programDirectory.getVarTable().addVar(
            p[-1], "float", 1, "constant", constdir)
    if programDirectory.getVarTable().idExist(p[-1]):
        operandStack.add(p[-1])
        typeStack.add(
            programDirectory.getVarTable().getItem(p[-1]).returnType())
    else:
        print("Error en parámetros")
        exit()

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
        returnType = programDirectory.getVarTable().getItem(p[1]).returnType()
        if returnType != "int":
            print("Error:la variable contadora no es entera")
            exit()
        typeStack.add(returnType)
    else:
        print("Error: No se ha declarado la variable contadora")
        exit()


def p_for_endexpid(p):
    '''
    for_endexpid : 
    '''
    global id
    exp = operandStack.top()
    operandStack.pop()
    global vcontrol
    vcontrol = operandStack.top()
    tempQuad = quadruples.Quadruple(id, '=', vcontrol, '', exp)
    quadrupleList.append(tempQuad)
    id += 1


def p_for_endexpcond(p):
    '''
    for_endexpcond : 
    '''
    global id
    global vcontrol
    #expType = typeStack.pop()
    exp = operandStack.top()
    operandStack.pop()
    vfinal = 'vfinal'
    constdir = Memory.assignDir("constant", "constant", 1)
    tempQuad = quadruples.Quadruple(id, '=', vfinal, '', exp)
    programDirectory.getVarTable().addVar(vfinal, "int", 1, "constant", constdir)
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
    constdir = Memory.assignDir("constant", "constant", 1)
    programDirectory.getVarTable().addVar(1, "int", 1, "constant", constdir)
    tempQuad = quadruples.Quadruple(id, '+', vcontrol, 1, '')
    ty = createTemp()
    tempQuad.setResult(ty)
    quadrupleList.append(tempQuad)
    id += 1
    tempQuad = quadruples.Quadruple(id, '=', vcontrol, '', ty)
    quadrupleList.append(tempQuad)
    id += 1
    fin = jumpsStack.pop()
    ret = jumpsStack.pop()
    tempQuad = quadruples.Quadruple(id, 'goto', '', '', ret)
    quadrupleList.append(tempQuad)
    id += 1
    fill(fin, id)
    # operandStack.pop()

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
    vardir = Memory.assignDir(currScope, "int", 1)
    programDirectory.getVarTable().addVar(myTemp, "int", 1, currScope, vardir)
    return myTemp


def createTempFun(newType):
    global idTemp
    idTemp += 1
    myTemp = "temp" + str(idTemp)
    currScope = scopeList[len(scopeList)-1]
    vardir = Memory.assignDir(currScope, "int", 1)
    programDirectory.getVarTable().addVar(myTemp, newType, 1, currScope, vardir)
    return myTemp


def createParamTemp():
    global param
    param += 1
    myTemp = "param" + str(param)
    currScope = scopeList[len(scopeList)-1]
    # cambiar para enviar verdadero tipo
    vardir = Memory.assignDir(currScope, "int", 1)
    programDirectory.getVarTable().addVar(myTemp, "int", 1, currScope, vardir)
    return myTemp


def assignQuadruple():
    global id
    tempQuad = quadruples.Quadruple(id, '', '', '', '')
    tempQuad.setOperator(operatorStack)
    operatorStack.pop()
    tempQuad.setOperandLeft(operandStack)
    operandStack.pop()
    tempQuad.setResult(operandStack.top())
    operandStack.pop()
    quadrupleList.append(tempQuad)
    id += 1


def operationQuadruple():
    global id
    tempQuad = quadruples.Quadruple(id, '', '', '', '')
    typeL = typeStack.pop()
    typeR = typeStack.top()
    if CUBE.get(typeL) != None:
        result = CUBE.get(typeL).get(typeR).get(operatorStack.top())
        if result == -1:
            print("Error, no coinciden los tipos")
            exit()
        else:
            tempQuad.setValues(operandStack, operatorStack)
            tempOperand = createTempFun(result)
            operandStack.add(tempOperand)
            tempQuad.setResult(tempOperand)
            quadrupleList.append(tempQuad)
            id += 1
    else:
        print("error en el tipo de operador")
        exit()


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
    while operandStack.size() >= 1 and operatorStack.size() > 0:
        if operatorStack.top() == '=':
            assignQuadruple()
        else:
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

#f = open("ejemplo_aritmetico.ja", "r")
#print("Ejemplo arimético")
#case_TestCorrect = parser.parse(f.read())

#print("Ejemplo funciones")
#f2 = open("ejemplo_funciones.ja", "r")
#case_TestCorrect2 = parser.parse(f2.read())

#f3 = open("ejemplo_objetos.ja", "r")
#print("Ejemplo objetos")
#case_TestCorrect2 = parser.parse(f3.read())

#f4 = open("ejemplo_ciclos.ja", "r")
#print("Ejemplo ciclos")
#case_TestCorrect2 = parser.parse(f4.read())

#print("Ejemplo arrays")
#f5 = open("ejemplo_arreglos.ja", "r")
#case_TestCorrect2 = parser.parse(f5.read())

#f6 = open("ejemplo_boleanos.ja", "r")
#case_TestCorrect2 = parser.parse(f6.read())
#print("Ejemplo bool")

print("Ejemplo fibonacci")
f7 = open("fibonacciIterative.ja", "r")
case_TestCorrect2 = parser.parse(f7.read())


if (dError == True):
    #for quadruple in quadrupleList:
    #    print(quadruple.getId(), quadruple.getOperator(), quadruple.getOperandLeft(), quadruple.getOperandRight(), quadruple.getResult())
    maquinaVirtual = virtualMachine(
        programDirectory.returnDirectory(), quadrupleList, eraData)
    maquinaVirtual.virtualMachineStart()
else:
    print("Failed")

dError = True
