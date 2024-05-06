import re
from collections import Counter

def make_multiset(s):
    multiset = []
    for i in range(len(s)-1):
        make_str = s[i:i+2]
        
        if re.fullmatch(r"[a-zA-Z]{2}", make_str):
            multiset.append(make_str)

    return multiset

def solution(str1, str2):
        
    A = make_multiset(str1)
    A = [element.lower() for element in A]
    
    B = make_multiset(str2)
    B = [element.lower() for element in B]
        
    A_counter = Counter(A)
    B_counter = Counter(B)
    
    intersection = len(list((A_counter & B_counter).elements()))
    union = len(list((A_counter | B_counter).elements()))

    if union == 0:
        return 65536
    else:
        answer = int((intersection/union) * 65536)
    
    return answer