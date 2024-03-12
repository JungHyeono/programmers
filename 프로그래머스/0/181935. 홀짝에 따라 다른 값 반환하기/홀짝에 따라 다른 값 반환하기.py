def solution(n):
    answer = 0
    a = 0
    if n % 2 == 0:
        for i in range(1, int(n/2)+1):
            a = 2*i
            answer += a*a
    elif n % 2 == 1:
        for i in range(1, int((n+1)/2)+1):
            a = 2*i - 1
            answer += a
        
    return answer