def solution(myString, pat):
    result = ''
    for i in myString:
        if i == 'A':
            result += ''.join('B')
        else:
            result += ''.join('A')
            
    return int(pat in result)