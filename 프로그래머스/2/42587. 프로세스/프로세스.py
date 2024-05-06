def solution(priorities, location):
    start = priorities.index(max(priorities))
    answer = 0
    while 1:
        high_process = max(priorities)
        
        if priorities[start] == high_process:
            priorities[start] = 0
            answer += 1
            
            if location == start:
                break
        start += 1
        if start >= len(priorities):
            start = 0
    
    return answer
            
    