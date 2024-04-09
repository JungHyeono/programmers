def solution(elements):
    old_len = len(elements)
    elements = elements * 2
    answer = []
    
    for i in range(1, old_len+1):
        if i == 1:
            for i in range(old_len):
                answer.append(elements[i])      # 첫번째는 원소를 각각 다 넣기
                
        elif i == old_len :
            answer.append(sum(elements[:])/2)   # 마지막은 값을 sum해서 넣기
            
        else:
            for j in range(old_len):
                answer.append(sum(elements[j:i+j]))
    
    answer = len(list(set(answer)))
    
    return answer