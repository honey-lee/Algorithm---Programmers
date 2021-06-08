from pandas import DataFrame as df

# m 높이, n 폭 (문자열의 길이)
def solution(m, n, board):
    answer = 0
    pop_list = []
    for i in range(n-1):
        for j in range(m-1):
            if board[i][j] == board[i][j+1]:
                pop_list.append((i, j, board[i][j]))

    return  pop_list

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

# print(df(board))
print(board[0][2])
print(solution(m, n, board))