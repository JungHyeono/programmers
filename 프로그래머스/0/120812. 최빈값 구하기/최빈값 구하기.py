def solution(array):
    num = {}
    for i in array:
        try: num[i] += 1
        except: num[i] = 1
    if list(num.values()).count(max(num.values())) > 1:
        return -1
    else: return max(num, key = num.get)