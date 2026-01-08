import sys
input = sys.stdin.readline

lst = list(input().strip())
num = []

star_idx = lst.index("*")
lst[star_idx] = '0'

for i in range(12):
    if i % 2 == 0:
        num.append(int(lst[i]))
    else:
        num.append(3*int(lst[i]))

calc = sum(num)
if star_idx != 12:
    if star_idx % 2 == 0:
        answer = 10 - (calc+int(lst[12])) % 10
    else:
        answer = (calc+int(lst[12]))*3 % 10
else:
    answer = 10 - calc % 10

print(answer)