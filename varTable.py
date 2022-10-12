# Var Table
class VariableTable:
    
    def __init__(self):
        global table
        table = [[]] #empty matrix
    
    def idExist(self, id) :
        if id in table:
            return True
        return False

    def validateType(self, type) :
        if type != 'object'  and type != 'int'  and type != 'float' and type != 'bool':
            return False
        return True   

    def addFunction(self, id, type, size, dir) :
        if(self.validateType(type) and not self.idExist(id)):
            newVar = {'id': id, 'type': type, 'size': size, 'dir': dir}
            table.append(newVar)