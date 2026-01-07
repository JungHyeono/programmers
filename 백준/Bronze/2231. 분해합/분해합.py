n = int(input())
    
answer = 0

def sum_digit(number):
    return sum(map(int,str(number)))

for i in range(1,n):
    if i+sum_digit(i) == n:
        answer = i
        break
    
print(answer)
