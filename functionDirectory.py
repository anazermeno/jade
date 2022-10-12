# Function Directory
class FunctionDirectory:
    
    def __init__(self):
        global directory
        directory = {'id': '', 'type': '', 'varsDirectory': {}}

    def validateType(self, type) :
        if type != 'function' and type != 'class' and type != 'object'  and type != 'int'  and type != 'float':
            return False
        return True   

    def idExist(self, id) :
        if id in directory:
            return True
        return False
        
    def addFunction(self, id, type, vars) :
        if(self.validateType(type) and not self.idExist(id)):
            directoryTemp = {'id': id, 'type': type, 'varsDirectory': vars}
            directory.update(directoryTemp)

    def printContent(self):
        print(directory)


   # TODO: removeFunction