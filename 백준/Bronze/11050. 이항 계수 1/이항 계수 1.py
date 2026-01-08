import sys
input = sys.stdin.readline

n, k = map(int,input().split())
#n!/(n-k)!k!

def fact(num):
    calc = 1
    if(num > 1):
        for i in range(2,num+1):
            calc = calc * i
    else: return 1
    return calc

nCk = fact(n)/(fact(n-k)*fact(k))

print(int(nCk))