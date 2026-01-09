import sys
input = sys.stdin.readline

N = int(input().rstrip())
num = 665
count = 0

while True:
    num += 1
    if "666" in str(num):
        count += 1
        if count == N:
            print(num)
            break
