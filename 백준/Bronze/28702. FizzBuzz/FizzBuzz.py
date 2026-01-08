import sys
input = sys.stdin.readline

seq = [ input().strip() for _ in range(3)]

is_num = False

def FizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0 and num % 5 != 0:
        return "Fizz"
    elif num % 3 != 0 and num % 5 == 0:
        return "Buzz"
    else:
        return num


for i, s in enumerate(seq):
    if s.isdigit():
        is_num = True
        digit_idx = i
        
if is_num:
    num_idx = 3 - seq.index(seq[digit_idx])
    num_find = int(seq[digit_idx]) + num_idx

    print(FizzBuzz(num_find))
    
    
else:
    print("FizzBuzz")