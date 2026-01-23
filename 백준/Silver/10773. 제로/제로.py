import sys
input = sys.stdin.readline

n = int(input())

num = []

for i in range(n):
    s = int(input())
    if s != 0:
        num.append(s)
    else:
        num.pop()
    
print(sum(num))
    