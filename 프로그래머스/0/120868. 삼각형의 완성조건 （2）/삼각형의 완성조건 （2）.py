def solution(sides):
    sides.sort()
    s, l = sides[0], sides[1]
    c1 = l - s + 1
    c2 = l + s - 1
    return c2-c1+1
        
        