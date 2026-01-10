import sys
input = sys.stdin.readline

N = int(input().rstrip())

people = []

for _ in range(N):
    age, name = input().split()
    people.append((int(age), name))

people.sort(key = lambda x : x[0])

for x,y in people:
    print(x,y)