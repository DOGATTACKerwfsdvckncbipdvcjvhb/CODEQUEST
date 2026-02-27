import sys

testcases = int(sys.stdin.readline().rstrip())
answer = ""
for i in range(testcases):
    x, y, z = map(float, sys.stdin.readline().rstrip().split(" "))
    answer += f"{x-180}, {y-180}, {z-180}\n"
print(answer)