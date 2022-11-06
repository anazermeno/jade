# 999 - 5,999 <-- global vars
# 6,000 - 10,999 <-- local vars
# 11,000 - 15,999 <-- temp vars
# 16,000 - 20,999 <-- constant vars
from stack import Stack

class Memory:
    i = []
    f = []

    def addInt(self, newInt : int):
        self.i.append(newInt)
        
    def addFloat(self, newFloat : float):
        self.i.append(newFloat)

    def resetVars(self):
        while self.i.count > 0:
            self.i.pop()

        while self.f.count > 0:
            self.f.pop()