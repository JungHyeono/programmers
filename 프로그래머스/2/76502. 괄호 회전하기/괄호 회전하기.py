def solution(s):
    ll = len(s)
    s = s*2
    count = 0
    
    for i in range(ll):
        new_string = s[i:i+ll]
        right = _match(new_string)
        if right == True:
            count += 1

    return count

def _match(new_string):
    stack = []
    ll = len(new_string)
    for i in range(ll):
        if new_string[i] == '[' or new_string[i] == '{' or new_string[i] == '(':
            stack.append(new_string[i])
        else:
            if len(stack) == 0:
                return False
            else:
                if new_string[i] == ']' and stack[-1] == '[':
                    stack.pop()
                elif new_string[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif new_string[i] == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
    if len(stack) != 0:
        return False
    return True