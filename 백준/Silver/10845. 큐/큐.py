import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
com = []
cque = deque()
for i in range(n):
    com.append(input().rstrip())

for c in com:
    if c[0:4] == "push":
        cque.append(int(c[4:]))
    elif c == "front":
        if cque:
            print(cque[0])
        else: print(-1)
    elif c == "back":
        if cque:
            print(cque[-1])
        else: print(-1)
    elif c == "pop":
        if cque:
            print(cque.popleft())
        else: print(-1)
    elif c == "size":
        print(len(cque))
    elif c == "empty":
        if cque: print(0)
        else: print(1)