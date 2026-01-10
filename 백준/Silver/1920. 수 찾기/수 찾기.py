import sys
input = sys.stdin.readline

N = int(input())

numbers = set(int(i) for i in input().split())

M = int(input())

for i in map(int,input().split()):
    if i in numbers:
        print("1",end='\n')
    else: print("0", end='\n')
