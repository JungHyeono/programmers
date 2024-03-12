def solution(n, control):
    answer = 0
    for i in control:
        if i == 'w': n += 1
        if i == 's': n -= 1
        if i == 'd': n += 10
        if i == 'a': n -= 10
    return n