import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

cnt = Counter(num)

m = int(input())
find = list(map(int, input().split()))

for i in find:
    print(cnt[i], end=' ')