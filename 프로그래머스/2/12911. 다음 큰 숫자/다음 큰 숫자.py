def solution(n):
    answer = n + 1          # n보다 큰 자연수
    
    n_cnt = bin(n)[2:].count('1')     # 2진수 n의 1의 개수를 셈.
    
    while not (bin(answer)[2:].count('1') == n_cnt and answer > n):
        answer += 1
        
    return answer
    