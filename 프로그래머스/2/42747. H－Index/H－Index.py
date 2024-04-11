def solution(citations):
    citations.sort(reverse = True)
    ll = len(citations)
    count = 0
    for h in range(ll):
        if citations[h] > h:
            count += 1
        else : break
    return count