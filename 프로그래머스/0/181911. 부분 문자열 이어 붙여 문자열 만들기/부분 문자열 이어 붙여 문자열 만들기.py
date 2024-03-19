def solution(my_strings, parts):
    answer = ''
    count = 0
    for s, e in parts:
        answer += my_strings[count][s:e+1]
        count += 1
    return answer