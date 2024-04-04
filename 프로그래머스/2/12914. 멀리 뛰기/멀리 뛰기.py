def solution(n):
    # a,b = 0,1
    # for i in range(n):
    #     a,b = b,a+b
    # return b % 1234567

    answer = [0, 1]
    
    for i in range(2, n+1):
        answer.append(answer[i-1] + answer[i-2])
    
    return (answer[-1]+answer[-2]) % 1234567
    