# Memory limits

# GLOBAL INT --> 1000 - 2999
# GLOBAL FLOAT --> 3000 - 4999
# GLOBAL BOOL --> 5000 - 6999

# LOCAL INT --> 7000 - 9999
# LOCAL FLOAT --> 10000 11999
# LOCAL BOOL --> 12000 13999

# CONSTANTS -->  14000 - 15999

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

CONSTANTS = 9000

MAX_PER_VAR = 2000

from stack import Stack

class multiDimensionVar:
    limInf : int
    limSup : int
    dim : int
    nextDim : bool

class MemoryRegistry:
    name : str
    type : str
    scope : str
    memoryAddress : int
    size : int 
    dimension : multiDimensionVar

    def __init__(self, name, type, scope, memoryAddress, size, dimension):
        self.name = name
        self.type = type
        self.scope = scope
        self.memoryAddress = memoryAddress
        self.size = size
        self.dimension = dimension

class Memory:
    # Arrays for Global int, Global float, Local int, Local float, Constants
    # Function with param var type, var scope and return var direction, updates var, and add to stack
    GLOBAL_INT : Stack
    GLOBAL_FLOAT : Stack
    GLOBAL_BOOL : Stack
    LOCAL_INT : Stack
    LOCAL_FLOAT : Stack
    LOCAL_BOOL : Stack
    CONSTANTS : Stack

    memory = [GLOBAL_INT, GLOBAL_FLOAT, LOCAL_INT, LOCAL_FLOAT, CONSTANTS]

    # Each element of the stacks contains a object MemoryRegistry that has name, type, memory address, space and dimension

    def addGlobalInt(self, newGlobalInt : MemoryRegistry):
        self.memory[0] = newGlobalInt
    
    def addGlobalFloat(self, newGlobalFloat : MemoryRegistry):
        self.memory[1] = newGlobalFloat

    def addLocalInt(self, newLocalInt : MemoryRegistry):
        self.memory[2] = newLocalInt

    def addLocalFloat(self, newLocalFloat : MemoryRegistry):
        self.memory[3] = newLocalFloat
    
    def addConstant(self, constant : MemoryRegistry):
        self.memory[4] = constant

    # Individual functions to clean stacks
    def resetGlobalInt(self):
        while self.memory[0].size() > 0:
            self.memory[0].pop()
    
    def resetGlobalFloat(self):
        while self.memory[1].size() > 0:
            self.memory[1].pop()

    def resetLocalInt(self):
        while self.memory[2].size() > 0:
            self.memory[2].pop()

    def resetLocalFloat(self):
        while self.memory[3].size() > 0:
            self.memory[3].pop()

    def resetConstants(self):
        while self.memory[4].size() > 0:
            self.memory[4].pop()

def assignDir(scope : str, type : str):
    global GLOBAL_INT, GLOBAL_FLOAT, GLOBAL_BOOL
    global cGLOBAL_INT, cGLOBAL_FLOAT, cGLOBAL_BOOL
    global LOCAL_INT, LOCAL_FLOAT, LOCAL_BOOL
    global cLOCAL_INT, cLOCAL_FLOAT, cLOCAL_BOOL

    if scope == "program":
        if type == "int":
            GLOBAL_INT += 1
            cGLOBAL_INT += 1
            return GLOBAL_INT
        elif type == "float":
            GLOBAL_FLOAT += 1
            cGLOBAL_FLOAT += 1
            return GLOBAL_FLOAT
        elif type == "bool":
            GLOBAL_BOOL += 1
            cGLOBAL_BOOL += 1
            return GLOBAL_BOOL
    elif scope == "local":
        if type == "int":
            LOCAL_INT += 1
            cLOCAL_INT += 1
            return LOCAL_INT
        elif type == "float":
            LOCAL_FLOAT += 1
            cLOCAL_FLOAT += 1
            return LOCAL_FLOAT
        elif type == "bool":
            LOCAL_BOOL += 1
            cLOCAL_BOOL += 1
            return LOCAL_BOOL
    else:
        return 0 

# Function to clean Memory
def resetVars(memory : Memory):
    Memory.resetGlobalInt()
    Memory.resetGlobalFloat()
    Memory.resetLocalInt()
    Memory.resetLocalFloat()
    Memory.resetConstants()

