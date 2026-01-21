import sys
input = sys.stdin.readline

n = input().rstrip()

s = ''.join(reversed(n))
print(1) if n == s else print(0)