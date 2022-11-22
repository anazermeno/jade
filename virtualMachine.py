from varTable import VariableTable
from virtualMemory import Memory


class virtualMachine:
    def __init__(self, directory: VariableTable(), quadruples: list, eraData: list):
        self.directory = directory
        self.quadruples = quadruples
        self.eraData = eraData
        self.assignedVars = {}
        self.tempbreadcrumb = 0

    def jadeSum(self, left, right, opresult):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        result = 0
        try:
            if right[0:4] == "temp":
                rightDir = self.directory.getItem(right).returnDir()
        except:
            rightDir = right
            result += right        
        if left[0:4] == "temp":
            leftDir = self.directory.getItem(left).returnDir()
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
        if left[0:4] == "temp":
            leftDir = self.directory.getItem(left).returnDir()
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
        if right[0:4] == "temp":
            rightDir = self.directory.getItem(right).returnDir()
        if left[0:4] == "temp":
            leftDir = self.directory.getItem(left).returnDir()
        vara = 0
        varb = 0
        for i in self.assignedVars:
            if i == leftDir:
                vara += self.assignedVars.get(i)
            if i == rightDir:
                varb += self.assignedVars.get(i)
        obj = {self.directory.getItem(result).returnDir(): (vara * varb)}
        self.assignedVars.update(obj)

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
            print(
                "No se puede hacer la división porque es entre cero o no se ha asignado valor a la variable")
        else:
            obj = {self.directory.getItem(result).returnDir(): (vara/varb)}
            self.assignedVars.update(obj)

    def jadeGoSub(self):
        while self.quadruples[self.tempbreadcrumb].getOperator() != 'ENDFUN' and self.tempbreadcrumb < len(self.quadruples):
            self.ExecuteQuadruple(self.quadruples[self.tempbreadcrumb])
            self.tempbreadcrumb += 1

    def jadeGoto(self):
        while self.tempbreadcrumb < len(self.quadruples):
            self.ExecuteQuadruple(self.quadruples[self.tempbreadcrumb])
            self.tempbreadcrumb += 1

    def jadeEra(self):
        while self.tempbreadcrumb < len(self.quadruples):
            self.ExecuteQuadruple(self.quadruples[self.tempbreadcrumb])
            self.tempbreadcrumb += 1

    def jadeWrite(self, var):
        if var[0:4] == "temp" or var.isdigit() == False:
            content = self.directory.getItem(var).returnDir()
            print(self.assignedVars.get(content))
        else:
            if self.assignedVars.get(var) != None:
                print(self.assignedVars.get(var))
            else:
                print("Error: la variable que se intentó imprimir aún no tiene un valor")

    def ExecuteQuadruple(self, quadruple):
        #print(quadruple.getId(), quadruple.getOperator(), quadruple.getOperandLeft(), quadruple.getOperandRight(), quadruple.getResult())
        if quadruple.getOperator() == '+':
            return self.jadeSum(quadruple.getOperandLeft(), quadruple.getOperandRight(), quadruple.getResult())
        elif quadruple.getOperator() == '-':
            return self.jadeSub(quadruple.getOperandLeft(),
                                quadruple.getOperandRight(), quadruple.getResult())
        elif quadruple.getOperator() == '*':
            return self.jadeMult(quadruple.getOperandLeft(),
                                 quadruple.getOperandRight(), quadruple.getResult())
        elif quadruple.getOperator() == '/':
            self.jadeDiv(quadruple.getOperandLeft(),
                         quadruple.getOperandRight(), quadruple.getResult())
        elif quadruple.getOperator() == '=':
            dir = self.directory.getItem(
                quadruple.getOperandLeft()).returnDir()
            obj = {dir: quadruple.getResult()}
            self.assignedVars.update(obj)
        elif quadruple.getOperator() == 'PARAM':
            print("parámetro", quadruple.getOperandLeft(), quadruple.getResult())
        elif quadruple.getOperator() == 'print':
            self.jadeWrite(quadruple.getResult())

    def virtualMachineStart(self):
        # look for assignment of global variables
        for i in range(0, self.quadruples[0].getResult()):
            if self.quadruples[i].getOperator() == '=':
                dir = self.directory.getItem(
                    self.quadruples[i].getOperandLeft()).returnDir()
                obj = {dir: self.quadruples[i].getResult()}
                self.assignedVars.update(obj)

        for quadruple in self.quadruples:
            if quadruple.getOperator() == 'goto':
                self.tempbreadcrumb = quadruple.getResult()
                self.jadeGoto()
            elif quadruple.getOperator() == 'GOSUB':
                self.tempbreadcrumb = quadruple.getResult()
                self.jadeGoSub()

