import sys
input = sys.stdin.readline

m, n = map(int, input().split())

num = [True]*1000001
num[1] = False

for i in range(2, int(n**(1/2))+1):
    if not num[i]: continue
    for j in range( i*2, n+1, i):
        num[j] = False

for k in range(m, n+1):
    if num[k]:
        print(k)