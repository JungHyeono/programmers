n = int(input())
cloth_size = list(map(int, input().split()))
t, p = map(int, input().split())

t_count = 0

for i in cloth_size:
    if i:
        t_count += (i // t) + (0 if (i%t) == 0 else 1)
print(t_count)
print(int(n/p),n%p)