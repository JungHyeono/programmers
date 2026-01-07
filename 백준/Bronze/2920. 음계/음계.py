n = list(map(int, input().split()))
count = 0
for i in range(1,len(n)):
    if n[i-1] - n[i]== 1:
        count -= 1
    elif n[i-1] - n[i] == -1:
        count += 1
    else:
        pass
if count == 7:
    print("ascending")
elif count == -7:
    print("descending")
else:
    print("mixed")