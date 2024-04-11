# def solution(n, left, right):
#     answer = []
#     for i in range(n):
#         for j in range(n):
#             answer.append(max(i+1, j+1))
    
#     return answer[left:right+1]
    
    
def solution(n, left, right):
    answer = []
    for idx in range(left, right+1):

        i, j = divmod(idx, n)           # idx를 n으로 나눈 몫과 나머지를 이용하여 행과 열 계산

        answer.append(max(i+1, j+1))    # 주어진 규칙에 따라 값 계산 및 추가
        
    return answer
    