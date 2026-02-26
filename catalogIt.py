import sys
import math

class Family:
    def __init__(self, parent, level):
        self.parent = parent
        self.level = int(level)


#
#
#

#


# def findChildren(objects, targetParent):
    




products = {}

answer = ""

testcases = int(sys.stdin.readline().rstrip())


for i in range(testcases):
    line = (sys.stdin.readline().rstrip()).split(",")
    products[line[0]] = Family(line[1],int(0))
    
productNames = sorted(products.keys()) ## sort wont work because it gets A2100 from sort as it sorts everything childs included.




count = 1
old_count = 1



def findChildren(target, sublist):
    global count
    global answer
    for b in sublist:
        if products[b].parent == target:
            answer += f"{'-' * count}{b}\n" 
            count += 1
            last_point = target
            sublist.remove(b)
            findChildren(b, sublist)
    findChildren(last_point, sublist)




for product in productNames:
    if products[product].parent == 'None':
        answer += product + '\n'
        findChildren(product, productNames)


#
# 




    
    