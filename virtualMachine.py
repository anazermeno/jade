from varTable import VariableTable
from virtualMemory import Memory


class virtualMachine:
    def __init__(self, directory: VariableTable(), quadruples: list):
        self.directory = directory
        self.quadruples = quadruples
        self.memory = Memory()


    def jadeSum(self, left, right):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        print("aqui", leftDir, rightDir)

    def jadeSub(self, left, right):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        print("aqui", leftDir, rightDir)

    def jadeMult(self, left, right):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        print("aqui", leftDir, rightDir)

    def jadeDiv(self, left, right):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        print("aqui", leftDir, rightDir)

    def jadeRead(self, left, right):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        print("aqui", leftDir, rightDir)

    def jadeWrite(self, res):
        print("hola", res.getResult())             

    def virtualMachineStart(self):
        for quadruple in self.quadruples:
            if quadruple.getOperator() == '+':
                self.jadeSum(quadruple.getOperandLeft(), quadruple.getOperandRight())
            elif quadruple.getOperator() == '-':
                print("resta")
            elif quadruple.getOperator() == '*':
                print("multiplicacion")
            elif quadruple.getOperator() == '/':
                print("división")
            elif quadruple.getOperator() == '=':
                print("asignación")
            elif quadruple.getOperator() == 'ENDFUN':
                print("fin de funcion")  
            elif quadruple.getOperator() == 'ERA':
                print("era")
            elif quadruple.getOperator() == 'PARAM':
                print("parámetro")
            elif quadruple.getOperator() == 'GOSUB':
                print("gosub")
            elif quadruple.getOperator() == 'print':
                self.jadeWrite(quadruple)                                    