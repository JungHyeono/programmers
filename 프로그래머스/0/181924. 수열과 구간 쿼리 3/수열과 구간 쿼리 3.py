def solution(arr, queries):
    length = len(queries)
    for i in range(length):
        arr[queries[i][0]], arr[queries[i][1]] = arr[queries[i][1]], arr[queries[i][0]]
    return arr