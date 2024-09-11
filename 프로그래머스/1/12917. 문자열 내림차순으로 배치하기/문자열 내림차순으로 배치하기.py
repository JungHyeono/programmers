def solution(s):
    s = sorted(s,reverse=True)
    result = ''
    for i in s:
        result += i
    return(result)