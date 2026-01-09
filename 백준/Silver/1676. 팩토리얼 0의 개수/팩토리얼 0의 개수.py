import sys
input = sys.stdin.readline

N = int(input().rstrip())

print(N//5 + N//25 + N//125)
    