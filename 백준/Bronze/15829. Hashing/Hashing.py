r = 31
M = 1234567891

L = int(input())

alphabet = {}

for i, ch in enumerate('abcdefghijklmnopqrstuvwxyz', start = 1):
    alphabet[ch] = i

s = input()

answer = 0
for i in range(L):
    answer += ((alphabet[s[i]]*(r**i)) % M)
    
print(answer%M)