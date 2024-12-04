def solution(num, total):
    start = int((total-int((num**2-num)/2))/num)
    return [start + i for i in range(num)]
            