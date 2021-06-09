from pandas import DataFrame as df
ans = 0
def is_finished(m, n, board):
    for i in range(n-1):
        for j in range(m-1):
            if board[i][j] == board[i][j+1] and board[i][j].isupper():
                return False
            return True

# m 높이, n 폭 (문자열의 길이)
def solution(m, n, board):
    global ans
    answer = 0
    pop_list = []
    for i in range(n-1):
        for j in range(m-1):
            if board[i][j] == board[i][j+1]:
                pop_list.append((i, j, board[i][j]))

    for i in range(len(pop_list)):
        

    return pop_list

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

# print(df(board))
print(board[0][2])
print(solution(m, n, board))


