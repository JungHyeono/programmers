def solution(my_string):
    result = []
    switch = True
    temp = ''
    for i in my_string:
        if i != ' ':
            temp += i
        else:
            if temp != '':
                result.append(temp)
                temp=''
                
    if temp != '':
        result.append(temp)
        
    return result