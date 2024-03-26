def solution(num_list):
    count = -1
    
    for i in num_list:
        count += 1
        if i < 0:
            return count
    return -1