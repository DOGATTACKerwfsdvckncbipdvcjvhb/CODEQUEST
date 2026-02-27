import sys

testCases = int(sys.stdin.readline().rstrip())

answer = ''
for i in range(testCases):
    minued = 0
    subtrahend = 0
    difference = 2#random number for defining
    
    line = sys.stdin.readline().rstrip().split(",")
    
    if int(line[0]) > int(line[1]):
        minued = int(line[0])
        subtrahend = int(line[1])
    else:
        minued = int(line[1])
        subtrahend = int(line[0])
    while True:
        difference = minued - subtrahend
        answer+= f"{minued}-{subtrahend}={difference}\n"
        if difference == 0 and minued == 1 and subtrahend ==1:
            answer+= "COPRIME\n"
            break
        elif difference == 0:
            answer+= "NOT COPRIME\n"
            break
        else:
            if difference > subtrahend:
                minued = difference
            else:
                minued = subtrahend
                subtrahend = difference        
print("\n\n")
print(answer)