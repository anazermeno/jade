from varTable import VariableTable
from virtualMemory import Memory


class virtualMachine:
    def __init__(self, directory: VariableTable(), quadruples: list, eraData: list):
        self.directory = directory
        self.quadruples = quadruples
        self.eraData = eraData
        self.assignedVars = {}
        self.pointerGlobal = 0

    def jadeSum(self, left, right, opresult):
        leftDir = self.directory.getItem(left).returnDir()
        rightDir = self.directory.getItem(right).returnDir()
        result = 0
        try:
            if right[0:4] == "temp":
                rightDir = self.directory.getItem(right).returnDir()
                result += self.assignedVars.get(rightDir)
            else:
                result += self.assignedVars.get(rightDir)
        except:
            rightDir = right
            result += right
        try:
            if left[0:4] == "temp":
                leftDir = self.directory.getItem(left).returnDir()
                result += self.assignedVars.get(leftDir)
            else:
                temp = self.assignedVars.get(leftDir)
                try:
                    if temp[0:4] == "temp":
                        leftDir = self.directory.getItem(temp).returnDir()
                        result += self.assignedVars.get(leftDir)
                except:
                    result += self.assignedVars.get(leftDir)
        except:
            leftDir = left
            result += left
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

    def jadeGoSub(self, pointer):
        while self.quadruples[pointer].getOperator() != 'ENDFUN':
            self.ExecuteQuadruple(self.quadruples[pointer])
            pointer += 1

    def jadeGoto(self, pointer):
        while pointer <= self.pointerGlobal:
            if pointer < len(self.quadruples):
                self.ExecuteQuadruple(self.quadruples[pointer])
            pointer += 1    
        pointer = self.pointerGlobal        
       

    def jadeLogicOp(self, quadruple):
        leftDir = self.directory.getItem(
            quadruple.getOperandLeft()).returnDir()
        rightDir = self.directory.getItem(
            quadruple.getOperandRight()).returnDir()
        vara = self.assignedVars.get(leftDir)
        varb = self.assignedVars.get(rightDir)
        try:
            if vara[0:4] == "temp":
                rightDir = self.directory.getItem(vara).returnDir()
                vara = self.assignedVars.get(rightDir)
        except:
            print( end = '')
        try:
            if varb[0:4] == "temp":
                leftDir = self.directory.getItem(varb).returnDir()
                varb = self.assignedVars.get(leftDir)
        except:
            print( end = '')
        if quadruple.getOperator() == '>':
            obj = {self.directory.getItem(
                quadruple.getResult()).returnDir(): (vara > varb)}
        elif quadruple.getOperator() == '<':
            obj = {self.directory.getItem(
                quadruple.getResult()).returnDir(): (vara < varb)}
        elif quadruple.getOperator() == '<=':
            obj = {self.directory.getItem(
                quadruple.getResult()).returnDir(): (vara <= varb)}
        elif quadruple.getOperator() == '>=':
            obj = {self.directory.getItem(
                quadruple.getResult()).returnDir(): (vara >= varb)}
        elif quadruple.getOperator() == '==':
            obj = {self.directory.getItem(
                quadruple.getResult()).returnDir(): (vara == varb)}
        elif quadruple.getOperator() == '!=':
            obj = {self.directory.getItem(
                quadruple.getResult()).returnDir(): (vara != varb)}
        self.assignedVars.update(obj)

    def jadeWrite(self, var):
        try: 
            if var[0:4] == "temp":
                content = self.directory.getItem(var).returnDir()
                print(self.assignedVars.get(content)) 
            else:
                dir1 = self.assignedVars.get(self.directory.getItem(var).returnDir())
                dir2 = self.directory.getItem(dir1).returnDir()
                if self.assignedVars.get(var) != None:
                    print(self.assignedVars.get(dir2))
                else:
                    print(self.assignedVars.get(self.directory.getItem(var).returnDir()))
        except:
           print(self.assignedVars.get(self.directory.getItem(var).returnDir())) 

    def ExecuteQuadruple(self, quadruple):
        self.pointerGlobal += 1 
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
        elif quadruple.getOperator() == 'ERA':
            global currFun
            currFun = quadruple.getResult()
        elif quadruple.getOperator() == 'PARAM':
            for i in self.eraData:
                if i[0] == currFun:
                    obj = {self.directory.getItem(
                    i[1][0]).returnDir(): quadruple.getOperandLeft()}
                    self.assignedVars.update(obj)
        elif quadruple.getOperator() == '>' or quadruple.getOperator() == '<' or quadruple.getOperator() == '<=' or quadruple.getOperator() == ">=" or quadruple.getOperator() == "!=" or quadruple.getOperator() == "==":
            self.jadeLogicOp(quadruple)
        elif quadruple.getOperator() == 'goto':
            self.pointerGlobal = quadruple.getResult()
            self.jadeGoto(self.pointerGlobal)
        elif quadruple.getOperator() == 'gotoF':
            vartocheck = quadruple.getOperandLeft()
            vardir = self.directory.getItem(vartocheck).returnDir()
            if self.assignedVars.get(vardir) == False:
                self.pointerGlobal = quadruple.getResult()
                self.jadeGoto(self.pointerGlobal) 
        elif quadruple.getOperator() == 'GOSUB':
            self.jadeGoSub(quadruple.getResult())    
        elif quadruple.getOperator() == 'print':
            self.jadeWrite(quadruple.getResult())
        if self.pointerGlobal == len(self.quadruples):
            exit()      
        #print("pointer global: ", self.pointerGlobal, "cuad:", quadruple.getOperator(), quadruple.getOperandLeft(), quadruple.getOperandRight())    
         

    def virtualMachineStart(self):
        # look for assignment of global variables
        for i in range(0, self.quadruples[0].getResult()):
            if self.quadruples[i].getOperator() == '=':
                dir = self.directory.getItem(
                    self.quadruples[i].getOperandLeft()).returnDir()
                obj = {dir: self.quadruples[i].getResult()}
                self.assignedVars.update(obj)

        if self.quadruples[0].getOperator() == 'goto':
            self.pointerGlobal = self.quadruples[0].getResult()
            self.jadeGoto(self.pointerGlobal)            
