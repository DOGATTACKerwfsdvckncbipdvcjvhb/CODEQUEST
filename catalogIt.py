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
    
productNames = sorted(products.keys()) ## sort wont work because it gets A2100 from sort as it sorts everything childs included.



for thing in productNames:
    print(productNames)




    
    