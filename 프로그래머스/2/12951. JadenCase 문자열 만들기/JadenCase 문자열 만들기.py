def solution(s):
    a = s.split(' ')
    result = []
    for i in range(len(a)):
            if i == 0:
                result.append(a[i].capitalize())
            else:
                result.append(a[i].capitalize())
    return str(' '.join(result))