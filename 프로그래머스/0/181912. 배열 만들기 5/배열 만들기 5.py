def solution(intStrs, k, s, l):

    result = []

    count = 0
    
    for i in intStrs:
        sentence = ''
        for j in range(s, s+l):
            sentence += sentence.join(i[j])
        if int(sentence)>k:
            result.append(int(sentence))
    return result