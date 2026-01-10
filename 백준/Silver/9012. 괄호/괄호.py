import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    s = input().rstrip()
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                print("NO")
                break
            else:
                stack.pop()
    else:    
        if stack:
            print("NO")
        else:
            print("YES")