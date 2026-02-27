import sys
import math

class Obstacle:
    def __init__(self, frequency, column):
        self.frequency = frequency
        self.column = column

testcases = int(sys.stdin.readline().rstrip())
answer = ""

def race():
    track = ""
    pos = start_pos
    row = 1
    for dir in directions:
        line = template
        for r in rules:
            if row % r.frequency == 0:
                line = line[:r.column] + "o" + line[r.column + 1:]
        
        if dir == "R":
            if line[pos] != "|":
                pos += 1
        elif dir == "L":
            if line[pos - 2] != "|":
                pos -= 1

        if line[pos - 1] == "o":
            line[pos - 1] = "x"
            track += line + "\n"
            track += "You Crashed - GAME OVER\n"
            return track
        
        line = line[:pos] + "v" + line[pos+1:]
        track += line + "\n"
    
        row += 1
    track += "=" * (width + 2)
    track += "\nCourse Complete!\n"
    return track



for case in range(testcases):
    line = (sys.stdin.readline().rstrip()).split()
    width = int(line[0])
    length = int(line[1])
    start_pos = int(line[2])
    
    rules = []
    n_rules = int(sys.stdin.readline().rstrip())
    for a in range(n_rules):
        rule = (sys.stdin.readline().rstrip()).split()
        rules.append(Obstacle(int(rule[0]), int(rule[1])))
    
    directions = sys.stdin.readline().rstrip("\n")
    template = "|" + (width * " ") + "|"

    answer += ("=" * (width + 2)) + "\n"
    answer += template[:start_pos] + "v" + template[start_pos+1:] + "\n"
    answer += ("-" * (width + 2)) + "\n" 
    track = race()
    answer += track

print(answer)
    









    

        