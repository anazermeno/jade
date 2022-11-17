# Var Table
class VariableTable:

    def __init__(self):
        global table
        table = []  # empty matrix

    def idExist(self, id):
        for item in table:
            if item.id == id:
                return True
        return False

    # Function to validate type
    def validateType(self, type):
        if type != 'object' and type != 'int' and type != 'float' and type != 'bool':
            return False
        return True

    # Function to add variable to variable table
    def addVar(self, id, type, size, scope, dir=0):
        if (self.validateType(type) and not self.idExist(id)):
            newVar = varReg(id, type, size, scope, dir)
            table.append(newVar)

    def printContent(self):
        for item in table:
            item.printItem()

    def getItem(self, id):
        for item in table:
            if item.id == id:
                return item
        return False


class varReg:

    def __init__(self, id, type, size, scope, dir=0):
        self.id = id
        self.type = type
        self.size = size
        self.scope = scope
        self.dir = dir

     # Function to get ID
    def setId(self, id):
        self.id = id

    # Function to retrieve ID
    def returnId(self):
        return self.id

    # Function to retrieve ID
    def returnScope(self):
        return self.scope

    # Function to get type
    def setType(self, type):
        self.type = type

    # Function to retrieve type
    def returnType(self):
        return self.type

    # Function to retrieve type
    def returnDir(self):
        return self.dir

    def printItem(self):
        print(self.id, self.type, self.size, self.scope, self.dir)
