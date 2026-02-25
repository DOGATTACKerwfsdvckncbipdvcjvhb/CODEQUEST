import sys
import math

alphabet = "abcdefghijklmnopqrstuvwxyz"

testCases = int(sys.stdin.readline().rstrip())

answer = ""

for i in range(testCases):
    shift = int(sys.stdin.readline().rstrip())
    scrambled = sys.stdin.readline().rstrip()
    message = ""
    for a in scrambled:
        if a == ' ':
            message += a
        else:
            position = alphabet.index(a)
            message += alphabet[position - shift]
    answer += message + '\n'

print(answer.rstrip())