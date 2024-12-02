def solution(rank, attendance):
    a = list(zip(rank,attendance))
    a.sort()
    result = 0
    temp = 10000
    people = []
    for i,j in a:
        if j:
            people.append(i)
    for i in people[:3]:
        result += temp * rank.index(i)
        temp /= 100
    return result