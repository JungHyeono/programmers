def solution(l, r):
    _list = []
    k = 2**(len(str(r)))
    for j in range(k):
        num = int((format(j, 'b')))*5
        if num >= l and num != 0 and num <= r :
            _list.append(num)
    return [-1] if not _list else _list