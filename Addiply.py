import sys
#for code quest academy

testcases = int(sys.stdin.readline().rstrip())
answer = ""

for i in range(testcases):
    line = (sys.stdin.readline().rstrip()).split(" ")
    num1 = int(line[0])
    num2 = int(line[1])
    x = f"{num1 + num2} {num1 * num2}"
    answer += x + "\n"

print(answer.rstrip())
