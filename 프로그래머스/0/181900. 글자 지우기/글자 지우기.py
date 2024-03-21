def solution(my_string, indices):
    result = ''
    my_list = list(my_string)
    for i in indices:
        my_list[i] = 1
    for k in my_list:
        if k != 1:
            result += k
    
    return result