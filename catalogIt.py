import sys


products = {}

answer = ""

testcases = int(sys.stdin.readline().rstrip())


for i in range(testcases):
    line = (sys.stdin.readline().rstrip()).split(",")
    products[line[0]] = line[1]
    
productNames = sorted(products.keys()) 

target = ""
count = 1
sublist = productNames


for product in productNames:
    if products[product] == 'None':
        target = product
        break

def printHierarchy(target, depth):
    global answer
    answer += f"{'-' * depth}{target}\n"
    for b in sublist:
        if products[b] == target:
            printHierarchy(b, depth + 1)

printHierarchy(target, 0)

print(answer.rstrip()) 