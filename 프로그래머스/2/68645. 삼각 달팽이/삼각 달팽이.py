def solution(n):
    tri = [[0] * (i + 1) for i in range(n)]
    result = []
    num = 0
    x,y = -1,0
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            num += 1
            tri[x][y] = num
            
    for num in tri:
        result.extend(num)
        
    return result



    
    
        