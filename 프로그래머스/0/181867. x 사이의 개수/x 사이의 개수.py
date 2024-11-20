def solution(myString):
    temp = myString.split('x')
    answer = []
    for i in temp:
        answer.append(len(i))
    return answer