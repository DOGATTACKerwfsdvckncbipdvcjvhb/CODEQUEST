import sys 

n_testcases = int(sys.stdin.readline().rstrip())
answer = ""

for i in range(n_testcases):
    answer += sys.stdin.readline().rstrip() + '\n' 

print(answer.rstrip())


