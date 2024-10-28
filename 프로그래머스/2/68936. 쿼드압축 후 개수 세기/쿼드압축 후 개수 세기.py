def solution(arr):
    length = len(arr)
    answer = compress(arr, 0, 0, length)
    result=[0,0]
    for i in range(0, len(answer), 2) :
        if answer[i:i+2]==[1,0]:
            result[0] += 1
        else:
            result[1] +=1
        
    
    return result

def compress(arr, x, y, size):
    first_element = arr[x][y]
    
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != first_element:
                half = size // 2
                return (
                    compress(arr, x, y, half) + 
                    compress(arr, x, y + half, half) + 
                    compress(arr, x + half, y, half) + 
                    compress(arr, x + half, y + half, half)
                )
    
    return [1, 0] if first_element == 0 else [0, 1]
                
            
    
