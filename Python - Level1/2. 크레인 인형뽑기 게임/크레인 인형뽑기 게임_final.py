def solution(board, moves):
    answer = 0
    picked = []

    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i] - 1] != 0:
                if picked and picked[-1] == board[j][moves[i] - 1]:
                    picked.pop(-1)
                    answer += 2
                    board[j][moves[i] - 1] = 0
                    break
                else:
                    picked.append(board[j][moves[i] - 1])
                    board[j][moves[i] - 1] = 0
                    break
            else:
                continue

    return answer

#  4 3 1 1 3 2 4