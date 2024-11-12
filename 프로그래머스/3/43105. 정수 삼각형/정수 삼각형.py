def solution(tri):
    for row in range(len(tri) - 2, -1, -1):
        for col in range(len(tri[row])):
            tri[row][col] += max(tri[row + 1][col], tri[row + 1][col + 1])
    return tri[0][0]


    
    