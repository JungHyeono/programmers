def solution(id_list, report, k):
    l = len(id_list)    #id_list 총 길이
    trade_map = [[0] * l for i in range(l)]     #신고를 맵으로 표현
    enum = {name: idx for idx, name in enumerate(id_list)}  #id_list의 순열
    
    for num in report:  #신고 현황 & 중복 제거
        x, y = num.split(" ")
        x_idx = enum[x]
        y_idx = enum[y]
        trade_map[x_idx][y_idx] = 1
        
    row_sums = [sum(row) for row in trade_map]          #가로합
    col_sums = [sum(col) for col in zip(*trade_map)]    #세로합
    
    ban_idx = []    #정지된 id의 인덱스 찾기
    for i in range(len(col_sums)):
        if col_sums[i] >= k:
            ban_idx.append(i)
            
    result = [0 for _ in range(l)]
    for j in range(0,l):
        for idx in ban_idx:
            if trade_map[j][idx] == 1:
                result[j] += 1
    return result
        