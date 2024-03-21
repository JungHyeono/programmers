def solution(s, e):
    answer = []
    for i in range(e, s+1):
        answer.append(i)
    
    return answer[::-1]