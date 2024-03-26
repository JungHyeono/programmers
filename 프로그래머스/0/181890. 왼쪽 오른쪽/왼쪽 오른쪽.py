def solution(str_list):
    try:
        if str_list.index('l') < str_list.index('r'):
            return str_list[:str_list.index('l')]
        else:
            return str_list[str_list.index('r')+1:]
    except:
        try: 
            if str_list.index('l') > -1:
                return str_list[:str_list.index('l')]
            # elif str_list.index('r') > -1:
            #     return str_list[str_list.index('r'):]
        except:
            try:
                if str_list.index('r') > -1:
                    return str_list[str_list.index('r')+1:]
            except:
                return []
    return []