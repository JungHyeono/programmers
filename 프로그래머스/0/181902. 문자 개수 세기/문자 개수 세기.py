import string

def solution(my_string):
    answer = []
    gong = []
    for i in range(52):
        gong.append(0)
    alpha = string.ascii_uppercase + string.ascii_lowercase
    _dict = dict(zip(alpha,gong))
    
    for i in my_string:
        _dict[i] += 1
        
    for value in _dict.values():
        answer.append(value)
        
    return answer