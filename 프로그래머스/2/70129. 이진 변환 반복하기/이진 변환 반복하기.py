def solution(s):
    
    answer = []
    zero_count = 0
    bin_count = 0
    
    while s != '1':
        while '0' in s :
            s = s.replace('0', '', 1)
            zero_count += 1
        s = format(len(s), 'b')
        bin_count += 1
        
    answer.extend([bin_count, zero_count])
    
    return answer