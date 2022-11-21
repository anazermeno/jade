# Memory limits

# GLOBAL INT --> 1000 - 2999
# GLOBAL FLOAT --> 3000 - 4999
# GLOBAL BOOL --> 5000 - 6999

# LOCAL INT --> 7000 - 9999
# LOCAL FLOAT --> 10000 11999
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
LOCAL_BOOL = 10000
cLOCAL_BOOL = 0

CONSTANTDIR = 12000
cCONSTANTS = 0


class Memory:

    def assignDir(scope: str, type: str):
        global GLOBAL_INT, GLOBAL_FLOAT, GLOBAL_BOOL
        global cGLOBAL_INT, cGLOBAL_FLOAT, cGLOBAL_BOOL
        global LOCAL_INT, LOCAL_FLOAT, LOCAL_BOOL
        global cLOCAL_INT, cLOCAL_FLOAT, cLOCAL_BOOL
        global CONSTANTDIR

        if scope == "program":
            if type == "int" and GLOBAL_INT < 2999:
                GLOBAL_INT += 1
                cGLOBAL_INT += 1
                return GLOBAL_INT
            elif type == "float" and GLOBAL_FLOAT < 4999:
                GLOBAL_FLOAT += 1
                cGLOBAL_FLOAT += 1
                return GLOBAL_FLOAT
            elif type == "bool" and GLOBAL_BOOL < 6999:
                GLOBAL_BOOL += 1
                cGLOBAL_BOOL += 1
                return GLOBAL_BOOL
        elif scope == "local":
            if type == "int" and LOCAL_INT < 8999:
                LOCAL_INT += 1
                cLOCAL_INT += 1
                return LOCAL_INT
            elif type == "float" and LOCAL_FLOAT < 10999:
                LOCAL_FLOAT += 1
                cLOCAL_FLOAT += 1
                return LOCAL_FLOAT
            elif type == "bool" and LOCAL_BOOL < 11999:
                LOCAL_BOOL += 1
                cLOCAL_BOOL += 1
                return LOCAL_BOOL
        elif scope == "constant":
            if type == "constannt" and CONSTANTDIR < 13999:
                CONSTANTDIR += 1
                cCONSTANTS += 1
                return CONSTANTDIR
        else:
            return 0


class multiDimensionVar:
    limInf: int
    limSup: int
    dim: int
    nextDim: bool
