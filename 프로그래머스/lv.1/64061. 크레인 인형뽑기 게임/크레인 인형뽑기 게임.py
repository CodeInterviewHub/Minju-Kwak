def solution(board, moves):
    answer = 0
    dol = []
    print(f"board : {board} / moves : {moves}")
    for m in moves:
        for w in range(len(board)):
            if board[w][m-1] != 0:
                if len(dol) != 0:
                    if board[w][m-1] == dol[-1]:
                        answer += 1
                        del dol[-1]
                    else:
                        dol.append(board[w][m-1])
                else:
                    dol.append(board[w][m-1])
                board[w][m-1] = 0
                break
    return answer*2