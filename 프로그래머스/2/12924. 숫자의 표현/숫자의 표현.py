def solution(n):
            
    start = 1
    end = 1
    count = 1
    _sum = 1
        
    while end != n :
        if _sum == n :
            count += 1
            end += 1
            _sum += end

        elif _sum > n :
            _sum -= start
            start += 1

        else :
            end += 1
            _sum += end
            
        
    return count



# https://github.com/WooVictory/Ready-For-Tech-Interview/blob/master/Algorithm/%ED%88%AC%ED%8F%AC%EC%9D%B8%ED%84%B0%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98.md // 투포인터 알고리즘

# https://www.acmicpc.net/problem/2018 // 백준 같은문제