def solution(myStr):
    temp = ''
    result = []
    for i in myStr:
        if i in 'abc':
            if temp != '':
                result.append(temp)
                temp = ''
        else:
            temp += ''.join(i)
    if temp != '':
        result.append(temp)
    
    return result if result else ["EMPTY"]