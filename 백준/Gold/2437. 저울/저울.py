import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
nums.sort()

weight = 1

for num in nums:
    if num > weight:
        break
    weight += num

print(weight)