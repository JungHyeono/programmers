def solution(num_list):
    hol = 0
    jak = 0
    
    for i in range(len(num_list)):
        if i % 2 == 0:
            hol += num_list[i]
        else:
            jak += num_list[i]
    if hol > jak:
        return hol
    return jak