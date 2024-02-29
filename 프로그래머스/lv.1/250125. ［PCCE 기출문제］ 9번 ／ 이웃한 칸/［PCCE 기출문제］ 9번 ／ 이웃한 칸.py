def solution(board, h, w):
    # 런타임에러
    # answer = 0
    # if board[h][w] == board[h+1][w]:
    #     answer += 1
    # if board[h][w] == board[h][w+1]:
    #     answer += 1
    # if h > 0:
    #     if board[h][w] == board[h-1][w]:
    #         answer += 1
    # if w > 0:
    #     if board[h][w] == board[h][w-1]:
    #         answer += 1
    n = len(board)
    count = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    
    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        if 0 <= h_check < n and 0<= w_check <n and board[h][w] == board[h_check][w_check]:
            count += 1
    return count