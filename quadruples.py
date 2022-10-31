from inspect import stack
from unittest import result
from stack import Stack

class Quadruple:
    id : int
    operandLeft : str
    operandRight : str
    operator : str
    result : str
    tempCounter : int

    def __init__(self, id, operandLeft, operandRight, operator, result):
        self.id = id
        self.operandLeft = operandLeft
        self.operandRight = operandRight
        self.operator = operator
        self.result = result

    def setOperandLeft(self, operandPop : Stack) :
        self.operandLeft = operandPop.top()
    
    def setOperandRight(self, operandPop : Stack):
        self.operandRight = operandPop.top()
    
    def setOperator(self, operatorPop : Stack):
        self.operator = operatorPop.top()
    
def printQuadrupleList(quadrupleList : list):
    for x in quadrupleList:
        print (x.id, x.operator, x.operandLeft, x.operandRight, x.result),