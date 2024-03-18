def solution(my_string, queries):
    
    my_s = list(my_string)
    for i in queries:
        l = i[1]-i[0]
        for j in range(int(l/2)+1):
            my_s[i[0]+j], my_s[i[1]-j] = my_s[i[1]-j], my_s[i[0]+j]
        
    return ''.join(my_s)