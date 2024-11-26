def solution(myString):
    myString = myString.split('x')
    answer = []
    for i in myString:
        if len(i) != 0:
            answer.append(i)
    answer.sort()
        
    return answer