def solution(n, t, m, p):
    num = t*m
    result = ''
    Temp = '0123456789ABCDEF'
    
    for i in range(num+1):
        answer = ''
        if i == 0: answer += '0'
        while i:
            answer += Temp[i%n]
            i //= n
        result += answer[::-1]
    
    return result[p-1::m][0:t]

