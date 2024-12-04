def solution(quiz):
    answer = []
    for i in quiz:
        idx = i.index('=')
        sum = eval(i[:idx])
        if sum == int(i[idx+2:]):
            answer.append("O")
        else:
            answer.append("X")
            
    return answer
                    