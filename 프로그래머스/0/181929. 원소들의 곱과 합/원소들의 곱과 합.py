def solution(num_list):
    answer = 1
    for i in range(len(num_list)):
        answer *= num_list[i]
    return 1 if answer < (sum(num_list))**2 else 0
        