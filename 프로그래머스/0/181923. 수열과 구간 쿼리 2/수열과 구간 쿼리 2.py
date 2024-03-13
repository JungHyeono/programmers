def solution(arr, queries):
    N_arr = []

    for a, b, c in queries:
        num = []
        for i in range(len(arr[a:b+1])):
            if arr[a+i] > c :
                num.append(arr[a+i])
        if num:
            N_arr.append(min(num))
        else: N_arr.append(-1)
        
    return N_arr
        
