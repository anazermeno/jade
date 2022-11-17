from varTable import VariableTable
from virtualMemory import Memory


class virtualMachine:
    def __init__(self, directory: VariableTable(), quadruples: list):
        self.directory = directory
        self.quadruples = quadruples
        self.memory = Memory()
        self.assignedVars = {}

    def jadeSum(self, left, right):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        result = 0
        for i in self.assignedVars:
            if i == leftDir or i == rightDir:
                result += self.assignedVars.get(i) 
        print("Resultado Suma: ", result)

    def jadeSub(self, left, right):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        vara = 0
        varb = 0
        for i in self.assignedVars:
            if i == leftDir:
                vara += self.assignedVars.get(i)
            if i == rightDir:
                varb += self.assignedVars.get(i)     
        print("Resultado Resta: ", vara - varb)

    def jadeMult(self, left, right):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        print("aqui", leftDir, rightDir)

    def jadeDiv(self, left, right):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        vara = 0
        varb = 0
        for i in self.assignedVars:
            if i == leftDir:
                vara += self.assignedVars.get(i)
            if i == rightDir:
                varb += self.assignedVars.get(i)     
        print("Resultado División: ", vara/varb)

    def jadeRead(self, left, right):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        print("aqui", leftDir, rightDir)

    def jadeWrite(self, quadruple):
        print(quadruple.getOperandRight())
        #dir = self.directory.getItem(quadruple).returnDir()
        for i in self.assignedVars:
            if i == dir:
                print(self.assignedVars.get(i))   

    def virtualMachineStart(self):
        for quadruple in self.quadruples:
            if quadruple.getOperator() == '+':
                self.jadeSum(quadruple.getOperandLeft(), quadruple.getOperandRight())
            elif quadruple.getOperator() == '-':
                self.jadeSub(quadruple.getOperandLeft(), quadruple.getOperandRight())
            elif quadruple.getOperator() == '*':
                print("multiplicacion")
            elif quadruple.getOperator() == '/':
                self.jadeDiv(quadruple.getOperandLeft(), quadruple.getOperandRight())
            elif quadruple.getOperator() == '=':
                dir = self.directory.getItem(quadruple.getOperandRight()).returnDir()
                obj = {dir : quadruple.getOperandLeft()}
                self.assignedVars.update(obj)
            elif quadruple.getOperator() == 'ENDFUN':
                print("fin de funcion")  
            elif quadruple.getOperator() == 'ERA':
                print("era")
            elif quadruple.getOperator() == 'PARAM':
                print("parámetro")
            elif quadruple.getOperator() == 'GOSUB':
                print("gosub")
            elif quadruple.getOperator() == 'print':
                print("Aqui: ", quadruple.getOperator())
                self.jadeWrite(quadruple)                                    