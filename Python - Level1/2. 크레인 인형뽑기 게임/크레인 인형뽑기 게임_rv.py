board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

#2차원 배열 리스트에 접근하는 함수 선언
def solution(board, moves):
    doll_list = [0] * 5
    new_list = []
    cnt = 0

    for i in moves:
        if board[i-1][-1] != 0:
            new_list.append(board[i-1][-1])
        board[i - 1].pop()

    for i in new_list:
        doll_list[i-1] += 1

    #print(doll_list)


    for i in doll_list:
        if i >= 2:
            i -= 2
            cnt += 2
        else:
            continue

    return cnt

print(solution(board, moves))