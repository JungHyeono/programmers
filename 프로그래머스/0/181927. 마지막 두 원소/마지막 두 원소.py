def solution(num_list):
    _len = len(num_list)-1
    if num_list[_len] > num_list[_len-1]:
        num_list.append(num_list[_len] - num_list[_len-1])
        return num_list
    else:
        num_list.append(num_list[_len]*2)
        return num_list
    return 