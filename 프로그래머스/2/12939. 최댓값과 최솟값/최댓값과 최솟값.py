def solution(s):
    s_list = s.split(' ')
    s_list = list(map(int, s_list))
    _list = []
    _list.extend([min(s_list), max(s_list)])
    
    answer = f'{_list[0]} {_list[1]}'
    
    return answer