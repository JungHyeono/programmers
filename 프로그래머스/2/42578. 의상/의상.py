def solution(clothes):
    fashion = {} 
    for name, typeof in clothes:
        if typeof in fashion.keys():
            fashion[typeof] += [name]
        else:
            fashion[typeof] = [name]
    
    answer = 1 
    for key, value in fashion.items():
        answer *= (len(value)+1)
    return answer-1