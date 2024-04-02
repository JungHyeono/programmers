def solution(arr):
    answer = 1
    arr.sort()
    for i in range(1, len(arr)):
        for j in range(max(arr[i], arr[i-1]), (arr[i] * arr[i-1]) + 1):
            if j % arr[i] == 0 and j % arr[i-1] == 0:
                arr[i] = j
                break
    return arr[-1]