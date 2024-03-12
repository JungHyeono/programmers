def solution(code):
    mode = 0
    ret = ""
    _list = list(code)
    idx = len(code)
    for i in range(idx):
        if mode == 0:
            if _list[i] != "1" and i % 2 == 0:
                ret += _list[i]
            elif _list[i] == "1": mode = 1
        elif mode == 1:
            if _list[i] != "1" and i % 2 == 1:
                ret += _list[i]
            elif _list[i] == "1": mode = 0
    if ret == "":
        return "EMPTY"
    return ret

