def solution(numLog):
    result = ''
    for i in range(len(numLog)-1):
        count = numLog[i+1]-numLog[i]
        if count == 1 : result += 'w'
        elif count == -1 : result += 's'
        elif count == 10 : result += 'd'
        else : result += 'a'
    return result