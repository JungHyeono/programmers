def solution(n, k):
    answer = []
    count = 1
    while n >= k * count:
        answer.append(k * count)
        count += 1




    return answer