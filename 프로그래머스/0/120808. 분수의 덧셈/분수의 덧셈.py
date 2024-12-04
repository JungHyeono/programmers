import math
def solution(numer1, denom1, numer2, denom2):
    numer1 *= denom2
    numer2 *= denom1
    denom1 *= denom2
    num = numer1 + numer2
    gcd = math.gcd(num,denom1)
    return[num/gcd,denom1/gcd]