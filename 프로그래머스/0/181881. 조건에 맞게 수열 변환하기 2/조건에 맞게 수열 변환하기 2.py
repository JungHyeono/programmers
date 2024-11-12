def solution(arr):
    count = 0
    return calc(arr,count)

def calc(arr,count):
    before_arr = arr[:]
    arr = [i / 2 if i >= 50 and i % 2 == 0 else i * 2 + 1 if i < 50 and i % 2 != 0 else i for i in arr]

    if before_arr == arr:
        return count
    else : 
        count += 1
        return calc(arr,count)
    
    
    
