import sys
input = sys.stdin.readline

N = int(input().rstrip())

lst = []

for _ in range(N):
    lst.append(int(input().rstrip()))
lst.sort()
print( *lst, sep='\n')