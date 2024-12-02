def solution(arr):
    two = [1,2]
    while(1):
        if two[0] == len(arr):
            break
        elif two[1] == len(arr):
            break
        elif two[0] < len(arr) and len(arr) < two[1]:
            for i in range(two[1]-len(arr)):
                arr.append(0)
            break
        else:
            two[0] = two[0]*2
            two[1] = two[1]*2
            
    
    return arr