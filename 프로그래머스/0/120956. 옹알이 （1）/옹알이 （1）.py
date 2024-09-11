import re

def solution(babbling):
    count = 0
    pattern = re.compile("^(aya|ye|woo|ma)+$") 

    for s in babbling:
        if pattern.match(s):
            count += 1
            
    return count
