def solution(s): 
    stack = []
    
    for i in s:
        if len(stack) == 0:     #스택이 비어있을 때
            stack.append(i)
        elif stack[-1] == i:    #스택의 윗부분이 i와 같을 때
            stack.pop()
        else: stack.append(i)   #비어있지 않고 같지 않을 때
        
    if len(stack) == 0: return 1

    else: return 0 