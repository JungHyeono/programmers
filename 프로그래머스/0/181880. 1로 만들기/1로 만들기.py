def solution(num_list):
    count = 0
    for i in num_list:
        while i > 1:
            count += 1
            if i % 2 == 0:
                i = int(i/2)
            else:
                i = int((i-1)/2)
                
    return count