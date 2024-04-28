import math
def solution(n, s):
    answer = []
    if n > s :
        return [-1]
    
    for i in range(n):
        answer.append(math.ceil(s/n))
        
    if s % n != 0:
        for i in range(sum(answer)-s):
            answer[i] -= 1
        
    return(answer)