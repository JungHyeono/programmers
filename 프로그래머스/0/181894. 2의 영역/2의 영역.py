def solution(arr):
    try: 
        start_found = arr.index(2)
        end_found = len(arr) - arr[::-1].index(2) - 1
    except: return [-1]
    
    return arr[start_found:end_found+1]