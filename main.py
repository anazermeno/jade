# -------------------------------------------
# JADE
# Ana Lizbeth Zermeño Torres     A00824913
# Ana Carolina Arellano Alvarez  A01650945
# September 2022
# ------------------------------------------

# Import Lex and Yacc
from ply.lex import lex
from ply.yacc import yacc

# Tokens
reserved = {
    'program' : 'PROGRAM',
}

# Token declaration
tokens = [] + list(reserved.values())

# Ignore
t_ignore = ' \t'

# Token matching

# Definition of reserved words

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
lexer = lex()
    
# Parser

# Functions for each grammar rule

def p_empty(p):
     '''
     empty : 
     '''
     pass

# Error handler for illegal syntaxis
def p_error(p):
    print("Syntax error at " + str(p.value))
    global dError
    dError = False

# Build the parser
parser = yacc()
dError = True