import sys
input = sys.stdin.readline

n = int(input())

seq = []

for _ in range(n):
    seq.append(int(input()))
    
cnt = 0
result = []
number = []   # 실제 스택
chk = 0

while cnt < n:
    # push 해야 하는 경우
    if chk < seq[cnt]:
        chk += 1
        number.append(chk)
        result.append("+")
    else:
        # pop 가능한지 검사
        if not number or number[-1] != seq[cnt]:
            print("NO")
            sys.exit()
        number.pop()
        result.append("-")
        cnt += 1

# 여기까지 왔으면 가능한 경우
print("\n".join(result))