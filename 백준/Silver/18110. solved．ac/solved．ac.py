import sys
input = sys.stdin.readline

n = int(input())

num = [ int(input()) for _ in range(n) ]

if n == 0: print("0")
else:
    num.sort()
    num_range = int(len(num)*0.15+0.5)
    num = num[num_range:n-num_range]

    print(int(sum(num)/len(num)+0.5))