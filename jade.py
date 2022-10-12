# -------------------------------------------
# JADE
# Ana Lizbeth Zermeño Torres     A00824913
# Ana Carolina Arellano Alvarez  A01650945
# October 2022
# ------------------------------------------

# Import Lex and Yacc
from asyncio import create_subprocess_exec
from tkinter.tix import TCL_DONT_WAIT
import ply.lex as lex
from ply.yacc import yacc
from functionDirectory import FunctionDirectory
from semanticCube import CUBE
from varTable import VariableTable

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
    program : PROGRAM ID createDir block
    '''
    # aqui va el remove del dirFun

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

def p_createDir( p ):
    '''
    createDir : empty
    '''
    programDirectory = FunctionDirectory()

def p_statement( p ):
    '''
    statement : assign
              | write
              | read
              | condition
              | forloop
              | whileloop
              | class
              | expression
    '''

def p_var( p ):
    '''
    var : VAR type var2 SEMICOLON
    '''

def p_var2( p ):
    '''
    var2 : ID var3
    '''
    
    #programDirectory.addFunction(p[1], 'VAR', VariableTable()) # como ponemos el directorio?

def p_var3( p ):
    '''
    var3 : COMMA var2
         | OBRACKET CTEINT CBRACKET COMMA var2
         | empty
    '''

def p_type( p ):
    '''
    type : INT
         | FLOAT
         | BOOL
    '''

def p_assign( p ):
    '''
    assign : ASSIGN assign2 SEMICOLON
    '''

def p_assign2( p ):
    '''
    assign2 : ID OBRACKET CTEINT CBRACKET EQUAL funcall assign3
            | ID OBRACKET CTEINT CBRACKET EQUAL varvalue assign3 
            | ID EQUAL funcall assign3 
            | ID EQUAL varvalue assign3 
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
    condition2 : OPARENTHESIS expression CPARENTHESIS block condition3
    '''

def p_condition3( p ):
    '''
    condition3 : ELSEIF condition2
               | ELSE block
               | empty
    '''

def p_write( p ):
    '''
    write : PRINT OPARENTHESIS write2
    '''

def p_write2( p ):
    '''
    write2 : expression write3
           | CTESTRING write3
    '''

def p_write3( p ):
    '''
    write3 : COMMA write2
           | CPARENTHESIS SEMICOLON
    '''

def p_read( p ):
    '''
    read : READ ID SEMICOLON
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
    funcall : ID OPARENTHESIS funcall2 CPARENTHESIS SEMICOLON
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
    g_exp2 : GREATERTHAN m_exp
           | LESSTHAN m_exp
           | ISEQUAL m_exp
           | NOTEQUAL m_exp
           | empty
    '''

def p_m_exp( p ):
    '''
    m_exp : t m_exp2
    '''

def p_m_exp2( p ):
    '''
    m_exp2 : PLUS m_exp
           | MINUS m_exp
           | empty
    '''

def p_t( p ):
    '''
    t : f t2
    '''

def p_t2( p ):
    '''
    t2 : MULT t
       | DIV t
       | empty
    '''

def p_f( p ):
    '''
    f : OPARENTHESIS expression CPARENTHESIS
      | varvalue
      | expression
      | ID
    '''

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
    obj_declaration : CLASSID OBJID OPARENTHESIS params CPARENTHESIS SEMICOLON
    '''

def p_obj_method_access( p ):
    '''
    obj_method_access : OBJID DOT method SEMICOLON
    '''

def p_obj_attr_access( p ):
    '''
    obj_attr_access : OBJID DOT attribute SEMICOLON
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
    return : RETURN ID SEMICOLON
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

# Build the parser
parser = yacc()
dError = True

print("*Test case - correct")
text = '''
program test1 {
var int num, num1;
assign num = 2, num1 = 3;

print (num + num1);
}'''
case_TestCorrect = parser.parse(text)

if(dError == True):
    print("Success")
else:
    print("Failed")

dError = True

print("*Test case 2 - failed")
case_TestCorrect = parser.parse('''
program test2 {
fun int multi(int num1){
    var int a;
    assign a = 0;
    return a;

    //TODO: Check how to add instructions after return
    num1 * num1; 
}
}
''')

if(dError == True):
    print("Success")
else:
    print("Failed")

# Test for semantic cube
if CUBE[int][float][">"] != -1:
    print("valid")
else:
    print("invalid")