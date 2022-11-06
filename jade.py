# -------------------------------------------
# JADE
# Ana Lizbeth Zermeño Torres     A00824913
# Ana Carolina Arellano Alvarez  A01650945
# October 2022
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
from stack import Stack
import quadruples

operatorStack = Stack()
operandStack = Stack()
jumpsPop = Stack()
typePop = Stack()

quadrupleList = []

id = 0
idTemp = 0

# Tokens
reserved = {
    'program' : 'PROGRAM',
    'class'   : 'CLASS',
    'var'     : 'VAR',
    'assign'  : 'ASSIGN',
    'fun'     : 'FUN',
    'return'  : 'RETURN',
    'int'     : 'INT',
    'float'   : 'FLOAT',
    'bool'    : 'BOOL',
    'mod'     : 'MOD',
    'void'    : 'VOID',
    'if'      : 'IF',
    'else'    : 'ELSE',
    'elseif'  : 'ELSEIF',
    'in'      : 'IN',
    'or'      : 'OR',
    'and'     : 'AND',
    'read'    : 'READ',
    'print'   : 'PRINT',
    'for'     : 'FOR',
    'while'   : 'WHILE',
    'return'  : 'RETURN'
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
t_SEMICOLON    = r'\;'
t_COLON        = r'\:'
t_COMMA        = r'\,'
t_DOT          = r'\.'
t_PLUS         = r'\+'
t_MINUS        = r'-'
t_MULT         = r'\*'
t_DIV          = r'/'
t_OPARENTHESIS = r'\('
t_CPARENTHESIS = r'\)'
t_OBRACKET     = r'\['
t_CBRACKET     = r'\]'
t_OCURLY       = r'\{'
t_CCURLY       = r'\}'
t_LESSTHAN     = r'\<'
t_GREATERTHAN  = r'\>'
t_EQUAL        = r'\='
t_NOTEQUAL     = r'\!='
t_ISEQUAL      = r'\=='

     
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID') 
    return t

def t_CLASSID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID') 
    return t

def t_COBJID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID') 
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
    r'[a-zA-Z]'
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
def p_program( p ):
    '''
    program : PROGRAM createDir block
    '''    

def p_createDir( p ):
    '''
    createDir : ID
    '''
    # Create global directory
    global programDirectory 
    programDirectory = FunctionDirectory()
    programDirectory.setId(p[1])
    programDirectory.addFunction(programDirectory.returnId(), "program", 0)
    # Create scope stack
    global scopeStack
    scopeStack = Stack()
    scopeStack.add(programDirectory.returnId())

def p_block( p ):
    '''
    block : OCURLY block2 block3 block4 block5 CCURLY
    '''

def p_block2( p ):
    '''
    block2 : var block2
           | empty
    '''

def p_block3( p ):
    '''
    block3 : fun block3
           | empty
    '''

def p_block4( p ):
    '''
    block4 : statement block4
           | empty
    '''

def p_block5( p ):
    '''
    block5 : return
           | empty
    '''

def p_statement( p ):
    '''
    statement : assign
              | write
              | read
              | condition
              | forloop
              | whileloop
              | class
    '''
    
def p_var( p ):
    '''
    var : VAR varType var2 endOfExp
    '''

def p_varType( p ):
    '''
    varType : type
    '''
 
def p_var2( p ):
    '''
    var2 : varID var3
    ''' 
    
def p_varID( p ):
    '''
    varID : ID
    '''
    programDirectory.setId(p[1])

def p_var3( p ):
    '''
    var3 : setVar var2
         | OBRACKET varArray CBRACKET COMMA var2
         | setVar2
    '''     

def p_setVar2( p ):
    '''
    setVar2 : empty
    '''
    programDirectory.getVarTable(scopeStack.top()).addVar(programDirectory.returnId(), programDirectory.returnType(), 0, 0) 

def p_setVar( p ):
    '''
    setVar : COMMA
    '''
    programDirectory.getVarTable(scopeStack.top()).addVar(programDirectory.returnId(), programDirectory.returnType(), 0, 0) 

def p_varArray( p ):
    '''
    varArray : CTEINT
    '''
    size = p[1]
    programDirectory.getVarTable(scopeStack.top()).addVar(programDirectory.returnId(), programDirectory.returnType(), size, 0) 
    
def p_type( p ):
    '''
    type : INT
         | FLOAT
         | BOOL
    '''
    programDirectory.setType(p[1])

def p_assign( p ):
    '''
    assign : ASSIGN assign2 endOfExp
    '''

def p_assign2( p ):
    '''
    assign2 : ID OBRACKET CTEINT CBRACKET EQUAL funcall assign3
            | ID OBRACKET CTEINT CBRACKET EQUAL varvalue assign3 
            | ID EQUAL funcall assign3 
            | ID EQUAL opadd addOperand assign3 
    '''

def p_assign3( p ):
    '''
    assign3 : COMMA assign2
            | empty
    '''

def p_condition( p ):
    '''
    condition : IF condition2
    '''

def p_condition2( p ):
    '''
    condition2 : OPARENTHESIS expression CPARENTHESIS gotoF block condition3
    '''

def p_gotoF( p ):
    '''
    gotoF :
    '''
    operatorStack.add("gotoF")
    createQuadruple()

def p_condition3( p ):
    '''
    condition3 : ELSEIF condition2
               | ELSE block
               | empty
    '''

def p_write( p ):
    '''
    write : PRINT opadd OPARENTHESIS write2 CPARENTHESIS endOfExp
    '''

def p_write2( p ):
    '''
    write2 : expression write3
           | CTESTRING write3
    '''

def p_write3( p ):
    '''
    write3 : COMMA write2
           |  empty
    '''

def p_read( p ):
    '''
    read : READ ID endOfExp
    '''

def p_fun( p ):
    ''' 
    fun : FUN fun2 fun_addFun OPARENTHESIS params CPARENTHESIS block
    '''

def p_fun_addFun(p):
    '''
    fun_addFun : ID
    '''
    # aqui va la funcion

def p_fun2( p ):
    '''
    fun2 : type 
        | VOID
    '''

def p_funcall( p ):
    ''' 
    funcall : ID OPARENTHESIS funcall2 CPARENTHESIS endOfExp
    '''

def p_funcall2( p ):
    ''' 
    funcall2 : params
             | empty
    '''

def p_forloop( p ):
    '''
    forloop : FOR OPARENTHESIS ID IN forloop2 CPARENTHESIS block
    '''

def p_forloop2( p ):
    '''
    forloop2 : ID
             | CTEINT
    '''

def p_expression( p ):
    '''
    expression : t_exp expression2
    '''

def p_expression2( p ):
    '''
    expression2 : OR expression
                | empty
    '''

def p_t_exp( p ):
    '''
    t_exp : g_exp t_exp2
    '''

def p_t_exp2( p ):
    '''
    t_exp2 : AND t_exp
           | empty
    '''

def p_g_exp( p ):
    '''
    g_exp : m_exp g_exp2
    '''

def p_g_exp2( p ):
    '''
    g_exp2 : GREATERTHAN opadd m_exp
           | LESSTHAN opadd m_exp
           | ISEQUAL opadd m_exp
           | NOTEQUAL opadd m_exp
           | empty
    '''

def p_m_exp( p ):
    '''
    m_exp : t m_exp2
    '''

def p_m_exp2( p ):
    '''
    m_exp2 : PLUS opadd m_exp
           | MINUS opadd m_exp
           | empty
    '''
    if(p[1] == None):
        endOfExpresion()

def p_opadd( p ):
    '''
    opadd :
    '''
    if operatorStack.size() > 0:
        if validateOperator(p[-1], operatorStack.top()):
            createQuadruple()
    operatorStack.add(p[-1])

def p_t( p ):
    '''
    t : f t2
    '''

def p_t2( p ):
    '''
    t2 : MULT opadd t
       | DIV opadd t
       | empty
    ''' 
    if(p[1] == None):
        endOfExpresion()

def p_f( p ):
    '''
    f : addFBottom expression popFBottom
      | addOperand
    '''
    
def p_endOfExp( p ):
    '''
    endOfExp : SEMICOLON
    '''
    endOfExpresion()

def p_addOperand( p ):
    '''
    addOperand : varvalue
               | ID
    '''
    if p[1] != None:
        operandStack.add(p[1])

def p_addFBottom( p ):
    '''
    addFBottom : OPARENTHESIS
    '''
    operatorStack.addFakeBottom()

def p_popFBottom( p ):
    '''
    popFBottom : CPARENTHESIS
    '''
    operatorStack.popFakeBottom()

def p_params( p ):
    '''
    params : type ID params2
    '''

def p_params2( p ):
    '''
    params2 : COMMA params
            | empty
    '''

def p_whileloop( p ):
    '''
    whileloop : WHILE g_exp block
    '''

def p_varvalue( p ):
    '''
    varvalue : CTEINT
             | CTEFLOAT
             | CTESTRING
    '''
    operandStack.add(p[1])

def p_class( p ):
    '''
    class : CLASS ID OCURLY class2 class3 CCURLY
    '''

def p_class2( p ):
    '''
    class2 : attribute class2
             | empty
    '''

def p_class3( p ):
    '''
    class3 : method class3
           | empty
    '''

def p_obj_constructor( p ):
    '''
    obj_constructor : CLASSID ID OPARENTHESIS params CPARENTHESIS block
    '''

def p_obj_declaration( p ):
    '''
    obj_declaration : CLASSID OBJID OPARENTHESIS params CPARENTHESIS endOfExp
    '''

def p_obj_method_access( p ):
    '''
    obj_method_access : OBJID DOT method endOfExp
    '''

def p_obj_attr_access( p ):
    '''
    obj_attr_access : OBJID DOT attribute endOfExp
    '''

def p_method( p ):
    '''
    method : fun
    '''

def p_attribute( p ):
    '''
    attribute : var
    '''
    
def p_return( p ):
    '''
    return : RETURN ID endOfExp
    '''
    
def p_empty( p ):
     '''
     empty : 
     '''
     pass

# Error handler for illegal syntaxis
def p_error( p ):
    print("Syntax error at " + str(p.value))
    global dError
    dError = False

def createQuadruple():
    if operandStack.size() > 0:
        if operatorStack.top() == "=":
            assignQuadruple()
        elif operatorStack.top() == "print":
            printQuadruple()
        elif operatorStack.top() == "gotoF":
            gotoFQuadruple()    
        else:
            operationQuadruple()

def createTemp():
    global idTemp
    idTemp += 1
    myTemp =  "temp" + str(idTemp)
    return myTemp

def assignQuadruple():
    global id
    tempQuad = quadruples.Quadruple(id,'','','','')
    tempQuad.setValues(operandStack, operatorStack)
    quadrupleList.append(tempQuad)
    id += 1

def operationQuadruple():
    global id
    tempQuad = quadruples.Quadruple(id,'','','','')
    tempQuad.setValues(operandStack, operatorStack)
    tempOperand = createTemp()
    operandStack.add(tempOperand)
    tempQuad.setResult(tempOperand)
    quadrupleList.append(tempQuad)
    id += 1

def printQuadruple():
    global id
    tempQuad = quadruples.Quadruple(id,'','','','')
    tempQuad.setOperator(operatorStack)
    operatorStack.pop()
    tempQuad.setResult(operandStack.top())
    operandStack.pop()
    quadrupleList.append(tempQuad)
    id +=1

def gotoFQuadruple():
    global id
    tempQuad = quadruples.Quadruple(id,'','','','')
    tempQuad.setOperator(operatorStack)
    operatorStack.pop()
    tempQuad.setOperandLeft(operandStack)
    operandStack.pop()
    # result con pila de saltos
    quadrupleList.append(tempQuad)
    id += 1
    
def endOfExpresion():
    if operatorStack.size() > 0 and operatorStack.top() == "print":
        printQuadruple() 
    else:
        while operandStack.size() % 2 == 0 and operatorStack.size() > 0:
            createQuadruple()
       
    
# Build the parser
parser = yacc()
dError = True

print("*Test case - correct")
text = '''
program test1 {
    if ((a * b / d * e - c) > 1) {
        print(a);
    }

}'''
case_TestCorrect = parser.parse(text)

if(dError == True):
    quadruples.printQuadrupleList(quadrupleList)
    print(operandStack.items)
    print(operatorStack.items)
else:
    print("Failed")

dError = True