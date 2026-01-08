n, m = map(int, input().split())

na = []
ma = []
for i in range(1,n+1):
    if n % i == 0:
        na.append(i)

for i in range(1,m+1):
    if m % i == 0:
        ma.append(i)
        
gcd = max(set(na) & set(ma))
lcm = n * m // gcd

print(gcd)
print(lcm)