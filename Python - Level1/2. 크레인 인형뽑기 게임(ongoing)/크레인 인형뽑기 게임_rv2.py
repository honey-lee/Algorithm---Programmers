board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

#런타임에러 코드를 좀 더 간단하게 해보자

#2차원 배열 리스트에 접근하는 함수 선언
def solution(board, moves):
    new_list = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                new_list.append(board[i][move-1])
                break

    print(new_list)

    result = cnt = 0



    return result

print(solution(board, moves))