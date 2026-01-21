import sys
input = sys.stdin.readline

n = int(input())
com = []
cque = []
for i in range(n):
    com.append(input().rstrip())

for c in com:
    if c[0:4] == "push":
        cque.append(int(c[4:]))
    elif c == "pop":
        if cque:
            print(cque.pop())
        else: print(-1)
    elif c == "size":
        print(len(cque))
    elif c == "empty":
        if cque: print(0)
        else: print(1)
    elif c == "top":
        if cque:
            print(cque[-1])
        else: print(-1)