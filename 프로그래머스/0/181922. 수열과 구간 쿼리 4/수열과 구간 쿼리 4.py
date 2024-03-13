def solution(arr, queries):
    for s, e, k in queries:
        for i in range(len(arr[s:e+1])):
            if (s+i) % k == 0:
                arr[s+i] += 1
    return arr