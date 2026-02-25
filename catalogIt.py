import sys
import math

class Family:
    def __init__(self, children, parent):
        self.parent = parent
        self.children = children

products = {}

answers = ''

testcases = int(sys.stdin.readline().rstrip())


for i in range(testcases):
    line = (sys.stdin.readline().rstrip()).split(",")
    products[line[0]] = Family([], line[1])
    
productNames = sorted(products.keys())
answers += productNames[0]

for thing in productNames:
    




    
    