# Function Directory
class directorioFunciones:
    
    def __init__(self):
        global directory
        directory = {'id': '', 'type': '', 'vars': ''}

    def validateType(type) :
        if type != 'function' and type != 'class' and type != 'object'  and type != 'int'  and type != 'float':
            return False
        return True   

    def idExist(id) :
        if id in directory:
            return True
        return False
        
    def addFunction(self, id, type, vars) :
        if(self.validateType(type) and not self.idExist(id)):
            directoryTemp = {'id': id, 'type': type, 'vars': vars}
            directory.update(directoryTemp)