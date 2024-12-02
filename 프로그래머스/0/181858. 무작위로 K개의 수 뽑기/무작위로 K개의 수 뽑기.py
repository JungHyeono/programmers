def solution(arr, k):
    a = []
    for i in arr:
        if i not in a:
            a.append(i)
    result = a[:k]
    if k-len(a) > 0:
        for i in range(k-len(a)):
            result.append(-1)
        
    return result