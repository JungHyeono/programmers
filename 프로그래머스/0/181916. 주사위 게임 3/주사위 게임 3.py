def solution(a, b, c, d):
    
    count = {}
    _list = []
    _list.extend([a,b,c,d])
    
    for i in _list:
        try : count[i] += 1
        except : count[i] = 1
    
    _list = list(set(_list))
    if len(_list) == 1:
        return 1111 * _list[0]
    
    elif len(_list) == 2:
        if count[max(count, key = count.get)] == 3:
            return (10 * max(count, key = count.get) + min(count, key = count.get))**2
        
        else: return (_list[0]+_list[1]) * (_list[1] - _list[0])
    
    elif len(_list) == 3:
        k = 1
        for i in _list:
            if i != max(count, key = count.get):
                k *= i
        return k
            
    else: return min(_list)
    
