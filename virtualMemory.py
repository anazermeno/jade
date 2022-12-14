# Memory limits

# Agregar objetos
# GLOBAL INT --> 1000 - 2999
# GLOBAL FLOAT --> 3000 - 4999
# GLOBAL BOOL --> 5000 - 6999

# LOCAL INT --> 7000 - 8999
# LOCAL FLOAT --> 9000 11999
# LOCAL BOOL --> 12000 13999
# CONSTANTS -->  14000 - 15999

MAX_PER_VAR = 2000

GLOBAL_INT = 1000
cGLOBAL_INT = 0
GLOBAL_FLOAT = 3000
cGLOBAL_FLOAT = 0
GLOBAL_BOOL = 5000
cGLOBAL_BOOL = 0

LOCAL_INT = 7000
cLOCAL_INT = 0
LOCAL_FLOAT = 9000
cLOCAL_FLOAT = 0
LOCAL_BOOL = 11000
cLOCAL_BOOL = 0

CONSTANTDIR = 13000
cCONSTANTS = 0


class Memory:
    # global vars
    def sumGlobalInt():
        global cGLOBAL_INT
        cGLOBAL_INT +=1

    def getGlobalInt():
        return cGLOBAL_INT

    def sumGlobalFloat():
        global cGLOBAL_FLOAT
        cGLOBAL_FLOAT +=1

    def getGlobalFloat():
        return cGLOBAL_FLOAT  

    def sumGlobalBool():
        global cGLOBAL_BOOL
        cGLOBAL_BOOL +=1

    def getGlobalBool():
        return cGLOBAL_BOOL

    # local vars
    def sumLocalInt():
        global cLOCAL_INT
        cLOCAL_INT +=1

    def getLocalInt():
        return cLOCAL_INT

    def sumLocalFloat():
        global cLOCAL_FLOAT
        cLOCAL_FLOAT +=1

    def getLocalFloat():
        return cLOCAL_FLOAT  

    def sumLocalBool():
        global cLOCAL_BOOL
        cLOCAL_BOOL +=1

    def getLocalBool():
        return cLOCAL_BOOL              

    # constant vars
    def sumConstant():
        global cCONSTANTS
        cCONSTANTS +=1

    def getConstant():
        return cCONSTANTS 

    def assignDir(scope: str, type: str, size: int):
        global GLOBAL_INT, GLOBAL_FLOAT, GLOBAL_BOOL
        global cGLOBAL_INT, cGLOBAL_FLOAT, cGLOBAL_BOOL
        global LOCAL_INT, LOCAL_FLOAT, LOCAL_BOOL
        global cLOCAL_INT, cLOCAL_FLOAT, cLOCAL_BOOL
        global CONSTANTDIR
        global cCONSTANTS

        if scope == "global":
            if type == "int" and GLOBAL_INT < 2999:
                GLOBAL_INT += size
                return GLOBAL_INT
            elif type == "float" and GLOBAL_FLOAT < 4999:
                GLOBAL_FLOAT += size
                return GLOBAL_FLOAT
            elif type == "bool" and GLOBAL_BOOL < 6999:
                GLOBAL_BOOL += size
                return GLOBAL_BOOL
        elif scope == "local":
            if type == "int" and LOCAL_INT < 8999:
                LOCAL_INT += size
                return LOCAL_INT
            elif type == "float" and LOCAL_FLOAT < 10999:
                LOCAL_FLOAT += size
                return LOCAL_FLOAT
            elif type == "bool" and LOCAL_BOOL < 12999:
                LOCAL_BOOL += size
                return LOCAL_BOOL
        elif scope == "constant":
            if type == "constant" and CONSTANTDIR < 14999:
                CONSTANTDIR += size
                return CONSTANTDIR
        else:
            return 0


class multiDimensionVar:
    limInf: int
    limSup: int
    dim: int
    nextDim: bool
