import sys


testcases = int(sys.stdin.readline().rstrip())

def checkAnagram():
    for char in word1:
        if char not in word2:
            return False
    return True

answer = ""

for i in range(testcases):
    line = sys.stdin.readline().rstrip()
    start = line.index("\"")
    pair = line[1:start - 2].split(",")
    end = line.index("\"", start + 1)

    sentence1 = line[start + 1: end].split()
    sentence2 = line[end + 3: len(line) - 1].split()

    word1 = sentence1[int(pair[0]) - 1]
    word2 = sentence2[int(pair[1]) - 1]

    if checkAnagram() == True:
        answer += "Verified\n"
    else: 
        answer += "Intercepted\n"

print(answer.rstrip())


    


