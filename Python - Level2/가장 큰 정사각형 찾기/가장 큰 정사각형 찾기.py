"""
Brute Force 효율성 시간초과

"""

def if_max(size, board):

    for i in range(len(board)-size+1):
        for j in range(len(board[0])-size+1):
            cnt = 0
            for k in range(i, i + size):
                for l in range(j, j + size):
                    if board[k][l]:
                        cnt += 1
            if cnt == size ** 2:
                return True

    return False


def solution(board):

    # 행과 열의 갯수
    row = len(board)
    col = len(board[0])
    max_square = 0

    # 최대 정사각형의 크기는 행과 열중 작은 쪽의 크기
    if row > col:
        max_square = col
    elif row < col:
        max_square = row
    elif row == col:
        max_square = row

    if row == col == max_square:
        cnt = 0
        for i in range(row):
            cnt += board[i].count(1)
        if cnt == max_square ** 2:
            return max_square ** 2
        max_square -= 1

    for i in range(max_square, 1, -1):
        if if_max(max_square, board) == True:
            return max_square ** 2

    return 1


board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board2 = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
print(solution(board))
print(solution(board2))