import sys
input = sys.stdin.readline
from collections import deque

testcase = int(input())

for i in range(testcase):
    n, m = map(int, input().split())
    
    seq = list(map(int, input().split()))
    
    seq_deque = deque()
    
    for l,s in enumerate(seq):
        seq_deque.append((l,s))
    
    cnt = 0
    
    while True:
        cur = seq_deque[0]
        
        if any(cur[1] < x[1] for x in seq_deque):
            seq_deque.append(seq_deque.popleft())
        else:
            cnt += 1
            if cur[0] == m:
                print(cnt)
                break
            seq_deque.popleft()
    