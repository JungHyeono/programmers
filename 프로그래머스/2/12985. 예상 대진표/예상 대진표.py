import math

def solution(n,a,b):
    
    count = 0
    
    for i in range(math.ceil(n**(1/2))):
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        count += 1
        if a == b:
            return count