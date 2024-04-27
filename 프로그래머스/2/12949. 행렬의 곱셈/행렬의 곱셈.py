def solution(arr1, arr2):
    row = len(arr1)
    col = len(arr1[0])
    end = len(arr2[0])
    
    answer = [[0 for j in range(end)] for i in range(row)]
    
    for i in range(row):
        for j in range(end):
            for k in range(col):
                answer[i][j] += arr1[i][k] * arr2[k][j]    
    
    return answer