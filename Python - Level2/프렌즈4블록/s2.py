def solution(m, n, board):
    flag = False
    result = 0
    # 조작하기 쉬운 리스트 형태로 전환
    n_board = []
    for i in range(m):
        tmp = []
        for j in range(n):
            tmp.append(board[i][j])
        n_board.append(tmp)

    while flag == False:
    # 블록이 4개 모여서 터지는 구간 찾기
        pop_list = []
        for i in range(m-1):
            for j in range(n-1):
                ans = 0
                bl = n_board[i][j]
                tmp = []
                for k in range(i, i+2):
                    for l in range(j, j+2):
                        if bl == 0:
                            continue
                        if n_board[k][l] == bl:
                            ans += 1
                            tmp.append([k, l, n_board[k][l]])
                        if ans == 4:
                            for p in range(len(tmp)):
                                if tmp[p] not in pop_list:
                                    pop_list.append(tmp[p])

        # 터질 블록이 없으면 끝내기
        if not pop_list:
            flag = True
            for i in range(m):
                for j in range(n):
                    if not n_board[i][j]:
                        result += 1

        # 블록이 있으면 터뜨리고
        else:
            while pop_list:
                n_board[pop_list[0][0]][pop_list[0][1]] = 0
                pop_list.pop(0)
        #
        #내리고 빈자리 채우기
        for i in range(n):
            tmp = []
            for j in range(m):
                if n_board[j][i] != 0:
                    tmp.append(n_board[j][i])
                else:
                    for k in range(len(tmp)):
                        n_board[j-k][i] = tmp[len(tmp)-1-k]
                        n_board[j-k-1][i] = 0

    return result


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

print(solution(m, n, board))


