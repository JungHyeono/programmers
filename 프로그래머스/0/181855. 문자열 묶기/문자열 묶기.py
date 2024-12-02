def solution(strArr):
    length = [0] * 31
    for i in strArr:
        length[len(i)] += 1
    return max(length)