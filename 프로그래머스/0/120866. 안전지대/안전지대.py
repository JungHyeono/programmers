def solution(board):
    board_length = len(board)
    board2 = [[0] * board_length for _ in range(board_length)]
    
    directions = [
        (-1, 0), (-1, -1), (-1, 1),  # 위쪽 3방향
        (1, 0), (1, -1), (1, 1),    # 아래쪽 3방향
        (0, -1), (0, 1)             # 양옆 2방향
    ]
    
    for i in range(board_length):
        for j in range(board_length):
            if board[i][j] == 1:
                board2[i][j] = 1
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < board_length and 0 <= nj < board_length:
                        board2[ni][nj] = 1
    count = sum(row.count(0) for row in board2)
    return count