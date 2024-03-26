def solution(arr, idx):
    try: found = arr[idx:].index(1)+idx
    except : found = -1
    
    return found


