def solution(s):
    stack = []
    count = 0
    for i in s:
        print(i)
        if i == '(':
            stack.append(i)
        elif i == ')':
            try: stack.pop()
            except: return False
    
    return False if stack else True