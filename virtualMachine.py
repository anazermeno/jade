from varTable import VariableTable


class virtualMachine:
    def __init__(self, directory: VariableTable(), quadruples: list):
        self.directory = directory
        self.quadruples = quadruples

    def virtualMachineStart(self):
        print(self.directory.printContent())
        for quadruple in self.quadruples:
            currId = quadruple.getId()
            currOperator = quadruple.getOperator()
            currOpLeft = quadruple.getOperandLeft()
            currOpRight = quadruple.getOperandRight()
            currResult = quadruple.getResult()
            print(currId, currOperator, currOpLeft, currOpRight, currResult)

    def solveQuadruples(self):
        print("hello world")
