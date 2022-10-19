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

    def __init__(self, operandLeft, operandRight, operator, result):
        self.id = 1
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
    for x in range(len(quadrupleList)):
        print (quadrupleList[x]),