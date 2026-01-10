import sys
input = sys.stdin.readline

N = int(input().rstrip())

pos = []

for _ in range(N):
    x,y = map(int, input().split())
    pos.append((x,y))
    
pos.sort(key=lambda x: (x[1],x[0]))

for x, y in pos:
    print(x, y)
    