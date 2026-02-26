import sys
import math

class Family:
    def __init__(self, children, parent, level):
        self.parent = parent
        self.children = children
        self.level = int(level)


#
#
#

#


# def findChildren(objects, targetParent):
    




products = {}

answers = ""

testcases = int(sys.stdin.readline().rstrip())


for i in range(testcases):
    line = (sys.stdin.readline().rstrip()).split(",")
    products[line[0]] = Family([], line[1],int(0))
    
productNames = sorted(products.keys()) ## sort wont work because it gets A2100 from sort as it sorts everything childs included.


#stop wait run one of the coman


# for i in products:
#     level = 4
#     temp = products[i]
#     print(temp.parent)
#     count = 4
#     UpCount = 1
#     while count > 0:
        
#         if temp == 'None':
#             break
#         count-=1
#         UpCount+=1
        
#         #temp = temp.parent

#             for s in products:

#     level = UpCount
    
#     products[i].level = level



count = 1

def findChildren(target, sublist):
       
    for i in sublist:
        if products[i].parent == target:
            answer += f"{'-' * count}{i}" 
            count += 1
            last_point = target
            sublist.remove(i)
            findChildren(i)
    count = 1 
    findChildren(last_point)




# for i in productNames:
#     if i.parent == 'None':
#         answer += i + '\n'
#         break 


#
# 




    
    