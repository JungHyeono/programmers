def solution(lines):
    map = [0] * 201
    for s,e in lines:
        for i in range(s+100,e+100):
            map[i] += 1
    result = 0
    
    for j in map:
        if j >= 2:
            result += 1
    return result
    