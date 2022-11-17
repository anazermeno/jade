from functionDirectory import FunctionDirectory

class virtualMachine:
    def __init__(self, directory : FunctionDirectory(), quadruples : list, ip : int):
        self.directory = directory
        self.quadruples = quadruples
        self.ip = ip
    
    def virtualMachineStart(self):
        for quadruple in self.quadruples:
            currId =quadruple.getId()
            currOperator = quadruple.getOperator()
            currOpLeft= quadruple.getOperandLeft()
            currOpRight= quadruple.getOperandRight()
            currResult= quadruple.getResult()
            print(currId, currOperator, currOpLeft, currOpRight, currResult)
