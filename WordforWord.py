import sys
import math

testcases = int(sys.stdin.readline().rstrip())
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
occurences = {}


def customLen(word):
    length = 0
    for char in word:
        if char in alphabet: length += 1
    return length

def findMedian():
    length = len(word_lens)
    if length % 2 != 0:
        return word_lens[length//2]
    else:
        high = length / 2
        low = high - 1
        return (low + high) / 2
    
def findMode():
    maximums = []
    max_val = 0
    for i in occurences.keys():
        if occurences[i] > max_val:
            maximums = [str(i)]
            max_val = occurences[i]
        elif occurences[i] == max_val:
            maximums.append(str(i))
    return maximums




for case in range(testcases):
    n_lines = int(sys.stdin.readline().rstrip())
    text = ""
    word_lens = []
    for i in range(n_lines):
        line = sys.stdin.readline().rstrip()
        words = line.split(" ")
        for word in words:
            word_length = customLen(word)
            try:
                occurences[word_length] += 1
            except:
                occurences[word_length] = 1
            word_lens.append(customLen(word))
    average = round(sum(word_lens)/len(word_lens), 1)
    print(f"Average: {average}")
    print(f"Median: {findMedian()}")
    modes = findMode()
    comma_seperated = str(",".join(modes))
    mode_answer = "Mode: " + comma_seperated
    print(mode_answer)
    highest_len = max(word_lens)
    print(f"Range: {highest_len - min(word_lens)}")
    for a in range(1, highest_len + 1):
        try:
            count = occurences[a]
            print(f"{a}|{"x" * count}")
        except:
            print(f"{a}|")


        
        
        