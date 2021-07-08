"""
DP - tabulation으로 다시 풀었다!!!
"""

def solution(board):
    answer = 0
    if len(board) < 2 or len(board[0]) < 2:
        return 1

    test = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if not i or not j:
                test[i][j] = board[i][j]
            elif i and j:
                if not board[i][j]:
                    test[i][j] = 0
                else:
                    test[i][j] = min(test[i-1][j-1], test[i-1][j], test[i][j-1]) + 1
            if test[i][j] > answer:
                answer = test[i][j]

    return answer ** 2


board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board2 = [[0,0,1,1],[1,1,1,1]]

print(solution(board2))

"""

[0 1 1 1]
[1 1 2 2]
[1 2 2 3]
[0 0 ]


[0 1 1 1]
[1 1 2 2]
[1 2 2 3]
[0 1 2 3]

"""

