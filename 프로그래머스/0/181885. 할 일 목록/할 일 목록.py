def solution(todo_list, finished):
    answer =[]
    for a, b in zip(todo_list, finished):
        if b == 0:
            answer.append(a)
            
    return answer