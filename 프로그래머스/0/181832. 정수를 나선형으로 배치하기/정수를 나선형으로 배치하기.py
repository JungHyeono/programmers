def solution(n):
    arr = [[0] * n for i in range(n)]
    num = 0
    for i in range(n):
        num += 1
        arr[0][i] = num 
    x, y = 0,n-1
    num +=1
    for i in range(n-1, 0, -2):
        for _ in range(i):
            x += 1
            if arr[x][y] == 0:
                arr[x][y] = num
                num += 1

        for _ in range(i):
            y -= 1
            if arr[x][y] == 0:
                arr[x][y] = num
                num += 1

        for _ in range(i - 1):
            x -= 1
            if arr[x][y] == 0:
                arr[x][y] = num
                num += 1

        for _ in range(i - 1):
            y += 1
            if arr[x][y] == 0:
                arr[x][y] = num
                num += 1
    print(arr)
    return arr