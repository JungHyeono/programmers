from collections import Counter

def solution(k, tangerine):
    answer = Counter(tangerine)
    sort_answer = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    
    count = 0
    
    for i in sort_answer:
        k -= i[1]
        count += 1
        if k <= 0:
            break
            
    return count