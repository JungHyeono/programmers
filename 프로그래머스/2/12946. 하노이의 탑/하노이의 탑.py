def solution(n):
    result = []
    hanoi(n, 1, 3, 2, result)
    return result

def hanoi(n, start, end, via, result):
    if (n==1):
        result.append([start,end])
    else:
        hanoi(n-1, start, via, end, result)
        result.append([start,end])
        hanoi(n-1, via, end, start, result)