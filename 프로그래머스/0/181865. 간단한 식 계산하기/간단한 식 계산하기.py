def solution(bio):
    num = []
    temp = ''
    for i in bio:
        if i in '+-*':
            num.append(int(temp))
            temp = ''
            op = ''.join(i)
        elif i in '0123456789':
            temp += ''.join(i)
    num.append(int(temp))
    
    if op in '+':
        return num[0] + num[1]
    elif op in '-':
        return num[0] - num[1]
    else:
        return num[0] * num[1]