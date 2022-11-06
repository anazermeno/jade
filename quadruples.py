from inspect import stack
from unittest import result
from stack import Stack

class Quadruple:
    id : int
    operandLeft : str
    operandRight : str
    operator : str
    result : str

    def __init__(self, id, operator, operandLeft, operandRight, result):
        self.id = id
        self.operator = operator
        self.operandLeft = operandLeft
        self.operandRight = operandRight
        self.result = result

    def setOperandLeft(self, operandStack : Stack) :
        self.operandLeft = operandStack.top()
    
    def setOperandRight(self, operandStack : Stack):
        self.operandRight = operandStack.top()
    
    def setOperator(self, operatorStack : Stack):
        self.operator = operatorStack.top()

    def setResult(self, result : str):
        self.result = result
    
    def setValues(self, operandStack : Stack, operatorStack : Stack) :
        self.operandRight = operandStack.top()
        operandStack.pop()
        self.operandLeft = operandStack.top()
        operandStack.pop()
        self.operator = operatorStack.top()
        operatorStack.pop() 

    def getid(self):
        return self.id
    
    def getOperandLeft(self):
        return self.operandLeft

    def getOperandRight(self):
        return self.operandRight

    def getOperator(self):        
        return self.operator

def printQuadrupleList(quadrupleList : list):
    for x in quadrupleList:
        print (x.id, x.operator, x.operandLeft, x.operandRight, x.result),