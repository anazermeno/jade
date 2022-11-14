
# GLOBAL INT --> 1000 - 3000
# GLOBAL FLOAT --> 3000 - 5000
# LOCAL INT --> 5000 - 7000
# LOCAL FLOAT --> 7000 - 9000
# CONSTANTS --> 9000 - 10000

GLOBAL_INT = 1000
GLOBAL_FLOAT = 3000
LOCAL_INT = 5000
LOCAL_FLOAT = 7000
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
    memoryAddress : int
    space : int 
    dimension : multiDimensionVar

    def __init__(self, name, type, memoryAddress, space, dimension):
        self.name = name
        self.type = type
        self.memoryAddress = memoryAddress
        self.space = space
        self.dimension = dimension

class Memory:
    # Stacks for Global int, Global float, Local int, Local float, Constants
    GLOBAL_INT : Stack
    GLOBAL_FLOAT : Stack
    LOCAL_INT : Stack
    LOCAL_FLOAT : Stack
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

# Function to clean Memory
def resetVars(memory : Memory):
    Memory.resetGlobalInt()
    Memory.resetGlobalFloat()
    Memory.resetLocalInt()
    Memory.resetLocalFloat()
    Memory.resetConstants()

