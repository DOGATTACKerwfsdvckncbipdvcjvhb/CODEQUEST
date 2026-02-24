import sys
testcases = int(sys.stdin.readline().rstrip())
# wait commit first

answer = "" 


for i in range(testcases):
    line = (sys.stdin.readline().strip()).split(":")
    speed = float(line[0])
    distance = float(line[1])
    
    try:
        time = distance/speed
    except ZeroDivisionError:
        answer += "SAFE\n"
        continue

    if time <= 1:
        answer += "SWERVE\n"
    elif time <= 5:
        answer += "BRAKE\n"
    else:
        answer += "SAFE\n"    
print(answer.rstrip())

