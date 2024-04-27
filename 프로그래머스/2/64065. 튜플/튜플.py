from collections import Counter
def solution(s):
    s = s.replace("{", "")
    s = s.replace("}", "")
    s = s.split(",")
    tuples = Counter(s).most_common()
    
    answer = []
    
    for item in tuples:
        answer.append(int(item[0]))
    
    return answer