def solution(num_list):
    num_len = len(num_list)
    answer = 1
    
    if num_len >= 11:
        for i in num_list:
            answer += i
        answer -= 1
    else:
        for i in num_list:
            answer *= i
            
    return answer