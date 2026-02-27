import sys

testcases = int(sys.stdin.readline().rstrip())
answer = ""
for i in range(testcases):
    x, y, z = map(float, sys.stdin.readline().rstrip().split(" "))

    if x < 180:
        answer += f"{round(x+180.00,2)}"
    else:
        answer += f"{round(x-180.00,2)}"
    if y < 180:
        answer += f" {round(y+180.00,2)}"
    else:
        answer += f" {round(y-180.00,2)}"
    if z < 180:
        answer += f" {round(z+180.00,2)}\n"
    else:
        answer += f" {round(z-180.00,2)}\n"
    
print(answer)