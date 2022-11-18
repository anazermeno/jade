from varTable import VariableTable
from virtualMemory import Memory


class virtualMachine:
    def __init__(self, directory: VariableTable(), quadruples: list):
        self.directory = directory
        self.quadruples = quadruples
        self.memory = Memory()
        self.assignedVars = {}

    def jadeSum(self, left, right, opresult):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        result = 0
        for i in self.assignedVars:
            if i == leftDir or i == rightDir:
                result += self.assignedVars.get(i)
        obj = {self.directory.getItem(opresult).returnDir(): result}
        self.assignedVars.update(obj)

    def jadeSub(self, left, right, result):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        if right[0:4] == "temp":
            rightDir = self.directory.getItem(right).returnDir()
        vara = 0
        varb = 0
        for i in self.assignedVars:
            if i == leftDir:
                vara += self.assignedVars.get(i)
            if i == rightDir:
                varb += self.assignedVars.get(i)
        obj = {self.directory.getItem(result).returnDir(): (vara - varb)}
        self.assignedVars.update(obj)

    def jadeMult(self, left, right, result):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        print("aqui", leftDir, rightDir)

    def jadeDiv(self, left, right, result):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        vara = 0
        varb = 0
        for i in self.assignedVars:
            if i == leftDir:
                vara += self.assignedVars.get(i)
            if i == rightDir:
                varb += self.assignedVars.get(i)
        if varb == 0:
            print("No se puede hacer la división porque es entre cero o no se ha asignado valor a la variable")        
        else:
            obj = {self.directory.getItem(result).returnDir(): (vara/varb)}
            self.assignedVars.update(obj)

    def jadeRead(self, left, right):
        print("en read virtual machine")
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        print("aqui", leftDir, rightDir)

    def jadeWrite(self, var):
        if var[0:4] == "temp":
            content =  self.directory.getItem(var).returnDir()
            print(self.assignedVars.get(content))
        else:
            if self.assignedVars.get(var) != None:
                print(self.assignedVars.get(var))
            else:
                print("Error: la variable que se intentó imprimir aún no es definida")    

    def ExecuteQuadruple(self, quadruple):
        if quadruple.getOperator() == '+':
            return self.jadeSum(quadruple.getOperandLeft(),quadruple.getOperandRight(),quadruple.getResult())
        elif quadruple.getOperator() == '-':
            return self.jadeSub(quadruple.getOperandLeft(),
                                    quadruple.getOperandRight(), quadruple.getResult())
        elif quadruple.getOperator() == '*':
            print("multiplicacion")
        elif quadruple.getOperator() == '/':
            self.jadeDiv(quadruple.getOperandLeft(),
                             quadruple.getOperandRight(), quadruple.getResult())
        elif quadruple.getOperator() == '=':
            dir = self.directory.getItem(quadruple.getOperandLeft()).returnDir()
            obj = {dir: quadruple.getResult()}
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
            self.jadeWrite(quadruple.getResult())

    def virtualMachineStart(self):
        for quadruple in self.quadruples:
            self.ExecuteQuadruple(quadruple)