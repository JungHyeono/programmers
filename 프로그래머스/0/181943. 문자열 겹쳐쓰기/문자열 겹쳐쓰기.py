def solution(my_string, overwrite_string, s):
    overlen = len(overwrite_string)
    mylen = len(my_string)
    my_string = my_string[0:s] + overwrite_string + my_string[s+overlen:]
    answer = my_string
    return answer