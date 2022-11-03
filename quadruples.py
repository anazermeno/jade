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

    def setOperandLeft(self, operandPop : Stack) :
        self.operandLeft = operandPop.top()
    
    def setOperandRight(self, operandPop : Stack):
        self.operandRight = operandPop.top()
    
    def setOperator(self, operatorPop : Stack):
        self.operator = operatorPop.top()

    def setResult(self, result : str):
        self.result = result
    
    def setValues(self, operandPop : Stack, operatorPop : Stack) :
        self.operandRight = operandPop.top()
        operandPop.pop()
        self.operandLeft = operandPop.top()
        operandPop.pop()
        self.operator = operatorPop.top()
        operatorPop.pop() 

    def getOperandLeft(self):
        return self.operandLeft

    def getOperandRight(self):
        return self.operandRight

    def getOperator(self):        
        return self.operator

def printQuadrupleList(quadrupleList : list):
    for x in quadrupleList:
        print (x.id, x.operator, x.operandLeft, x.operandRight, x.result),