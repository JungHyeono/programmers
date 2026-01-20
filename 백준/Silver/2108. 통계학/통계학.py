import sys
input = sys.stdin.readline

n = int(input())
num = [ int(input()) for _ in range(n) ]

avg = int(round(sum(num)/n))

num.sort()

fre_num = [0] * 8001

for x in num:
    fre_num[x+4000] += 1

fre_cnt = max(fre_num)
modes = [i - 4000 for i, v in enumerate(fre_num) if v == fre_cnt]
modes.sort()


print(avg)
print(num[int(n/2)])
print(modes[0]) if len(modes) < 2 else print(modes[1])
print(num[n-1]-num[0])