import sys
import math

class Obstacle:
    def __init__(self):
        pass

testcases = int(sys.stdin.readline().rstrip())
answer = ""


for case in range(testcases):
    line = (sys.stdin.readline().rstrip()).split(" ")
    width = int(line[0])
    length = int(line[1])
    start_pos = int(line[2])

    rules = []
    n_rules = int(sys.stdin.readline().rstrip())
    for a in range(n_rules):
        rule = (sys.stdin.readline().rstrip()).split(" ")
        rules.append(Obstacle(rule[0]))
        