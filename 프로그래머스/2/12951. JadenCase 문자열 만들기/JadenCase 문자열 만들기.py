def solution(s):
    a = s.split(' ')
    result = []
    for i in range(len(a)):
            result.append(a[i].capitalize())
    return str(' '.join(result))