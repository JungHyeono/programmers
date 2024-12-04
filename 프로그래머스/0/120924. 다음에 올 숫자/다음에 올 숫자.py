def solution(common):
    diff = common[1] - common[0]
    for i in range(1,len(common)-1):
        if common[i+1] - common[i] == diff:
            return common[-1]+diff
        else:
            diff = int(common[i+1]/common[i])
            return common[-1] * diff