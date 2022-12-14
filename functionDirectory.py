# Function Directory
from varTable import VariableTable


class FunctionDirectory:

    def __init__(self):
        self.id = ''
        self.type = ''
        global directory
        directory = {}

    def validateType(self, type):
        if type != 'void' and type != 'local' and type != 'class' and type != 'object' and type != 'int' and type != 'float' and type != 'bool' and type != "program":
            return False
        return True

    def idExist(self, id):
        if id in directory:
            return True
        return False

    def addFunction(self, id, type, size):
        if (self.validateType(type) and not self.idExist(id)):
            directoryTemp = {
                id: {'type': type, 'size': size, 'varsTable': VariableTable()}}
            directory.update(directoryTemp)

    def getVarTable(self):
        return directory.get("program")["varsTable"]

    def emptyDirectory(self):
        directory.clear()

    def printContent(self):
        for item in directory["program"]:
            if item == "varsTable":
                print("VAR TABLE:")
                directory.get("program")["varsTable"].printContent()

    # Function to get ID
    def setId(self, id):
        self.id = id

    # Function to retrieve type
    def returnDirectory(self):
        return directory.get("program")["varsTable"]

    # Function to retrieve ID
    def returnId(self):
        return self.id

    # Function to get type
    def setType(self, type):
        self.type = type

    # Function to retrieve type
    def returnType(self):
        return self.type

   # TODO: removeFunction
