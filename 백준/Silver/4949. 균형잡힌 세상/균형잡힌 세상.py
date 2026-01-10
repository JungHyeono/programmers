import sys
input = sys.stdin.readline


while(True):
    gwal = []
    s = input().rstrip()
    
    if s == '.':
        break
    
    check = True
    
    for i in s:
        if i == '[' or i == '(':
            gwal.append(i)
        elif i == ')' and gwal:
            if '(' == gwal[-1]:
                gwal.pop()
            else: 
                check = False
                break
        elif i == ']' and gwal:
            if '[' == gwal[-1]:
                gwal.pop()
            else:
                check = False
                break
        elif not gwal and (i == ')' or i == ']'):
            check = False
            break
    if check and not gwal:
        print("yes")
    else:
        print("no")