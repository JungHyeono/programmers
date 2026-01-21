import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

deq = deque( range(1,n+1))
ans = []

while deq:
    for _ in range(k-1):
        deq.append(deq.popleft())
    ans.append(deq.popleft())
    
print("<" + ', '.join(map(str, ans)) + ">")