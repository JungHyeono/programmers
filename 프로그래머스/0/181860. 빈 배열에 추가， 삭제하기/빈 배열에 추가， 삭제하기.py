def solution(arr, flag):
    result = []
    for i,j in zip(arr, flag):
        if j == True:
            for k in range(i):
                result.append(i)
                result.append(i)
        else:
            if result:
                for p in range(i):
                    result.pop()
            
    return result