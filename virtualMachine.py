import virtualMemory
import stack
import quadruples
from functionDirectory import FunctionDirectory

class virtualMachine:
    def __init__(self, memory : virtualMemory, quadruples : list, ip : int):
        self.memory = memory
        self.quadruples = quadruples
        self.ip = ip
    
    def virtualMachineStart(self, functionDir : FunctionDirectory, quadruple : quadruples):
        for quadruple in self.quadruples:
            currId =quadruple.getId()
            currOperator = quadruple.getOperator()
            currOpLeft= quadruple.getOperandLeft()
            currOpRight= quadruple.getOperandRight()
            currResult= quadruple.getResult()
            print(currId, currOperator, currOpLeft, currOpRight, currResult)
