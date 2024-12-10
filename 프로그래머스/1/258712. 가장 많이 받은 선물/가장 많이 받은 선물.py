def solution(fri, gifts):
    l = len(fri)    #friends의 총 길이
    trade_map = [[0] * l for i in range(l)]     #선물 교환을 맵으로 표현
    enum = {name: idx for idx, name in enumerate(fri)}  #friends의 순열
    total = [0] * l     #사람별 선물 받는 개수
    
    for gift in gifts:
        x, y = gift.split(" ")
        x_idx = enum[x]
        y_idx = enum[y]
        trade_map[x_idx][y_idx] += 1
        
    row_sums = [sum(row) for row in trade_map]          #가로합
    col_sums = [sum(col) for col in zip(*trade_map)]    #세로합
    diff = [row_sums[i] - col_sums[i] for i in range(l)]    #선물 지수
        
    
    for i in range(1,l):
        for j in range(i):
            if trade_map[i][j] > trade_map[j][i]:
                total[i] += 1
            elif trade_map[i][j] < trade_map[j][i]:
                total[j] += 1
            else:
                if diff[i] > diff[j]:
                    total[i] += 1
                elif diff[i] < diff[j]:
                    total[j] += 1
    return max(total)
        