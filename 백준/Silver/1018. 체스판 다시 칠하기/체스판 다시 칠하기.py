import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for _ in range(n) ]


for i in range(n):
    s = input()
    for x in s:
        arr[i].append(x)
        
chess_x = n-7
chess_y = m-7


count_arr = []
for x in range(chess_x):
    for y in range(chess_y):
        w_count = 0
        b_count = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j) % 2 == 0:
                    if arr[i][j] != 'W':
                        w_count += 1
                if (i+j) % 2 == 1:
                    if arr[i][j] != 'B':
                        w_count += 1
                if (i+j) % 2 == 0:
                    if arr[i][j] != 'B':
                        b_count += 1
                if (i+j) % 2 == 1:
                    if arr[i][j] != 'W':
                        b_count += 1
        count_arr.append(min(w_count,b_count))
            
print(min(count_arr))