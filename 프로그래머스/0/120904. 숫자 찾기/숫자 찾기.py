def solution(num, k):
    na = 0
    answer = 0
    arr = []
    while (num > 0):
        na = num % 10
        arr.append(na)
        num = int(num / 10)
    
    arr.reverse()

    try:
        answer = arr.index(k) + 1
    except:
        return -1 
    return answer