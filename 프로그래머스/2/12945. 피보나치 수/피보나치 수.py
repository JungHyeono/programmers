def solution(n):
    answer = [0, 1]
    
    for i in range(2, n+1):
        answer.append(answer[i-1] + answer[i-2])
    
    return answer[-1] % 1234567
    
    
    # 밑은 더 좋은 방식의 코딩
    # a,b = 0,1
    # for i in range(n):
    #     a,b = b,a+b
    # return a % 1234567