def solution(dots):
    lines = []  # 결과를 저장할 리스트
    for i in range(len(dots)):
        for j in range(i + 1, len(dots)):  # 중복 계산 방지
            line = round((dots[j][1] - dots[i][1]) / (dots[j][0] - dots[i][0]),2)
            lines.append(line)
    for line in lines:
        if lines.count(line) == 2:
            return 1
        elif lines.count(line) ==6:
            return 1
    return 0

