import sys
input = sys.stdin.readline

n = int(input())

count = [0] * 10001  # 1~10000

for _ in range(n):
    count[int(input())] += 1

for i in range(1, 10001):
    if count[i]:
        for _ in range(count[i]):
            print(i)