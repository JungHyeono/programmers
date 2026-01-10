import sys
input = sys.stdin.readline

N = int(input().rstrip())

pp = []

for _ in range(N):
    x, y = map(int, input().split())
    pp.append((x,y))
    
for i in range(N):
    rank = 1
    for j in range(N):
        if pp[i][0] < pp[j][0] and pp[i][1] < pp[j][1]:
            rank += 1
    print(rank, end =' ')