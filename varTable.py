# Var Table
class VariableTable:
    
    def __init__(self):
        global table
        table = [[]] #empty matrix
        
    def idExist(self, id) :
        if id in table:
            return True
        return False

    # Function to validate type
    def validateType(self, type) :
        if type != 'object'  and type != 'int'  and type != 'float' and type != 'bool':
            return False
        return True   
    
    # Function to add variable to variable table
    def addVar(self, id, type, size, dir = 0) :
        #if(self.validateType(type) and not self.idExist(id)):
        newVar = {'id': id, 'type': type, 'size': size, 'dir': dir}
        table.append(newVar)
        print(table)
    
    # Function to get ID
    def setId(self, id) :
        self.id = id

    # Function to retrieve ID
    def returnId(self) :
        return self.id

    # Function to get type
    def setType(self, type) :
        self.type = type
    
    # Function to retrieve type
    def returnType(self) :
        return self.type