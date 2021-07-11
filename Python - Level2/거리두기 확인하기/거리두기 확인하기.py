def solution(places):
    answer = [1 for _ in range(5)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 좌상 우상 좌하 우하
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    for i in range(5):
        for j in range(5):
            for k in range(5):
                if places[i][j][k] != 'P':
                    continue
                else:
                    for l in range(4):
                        for m in range(2):
                            new_j, new_k = j + (dr[l] * (m + 1)), k + (dc[l] * (m + 1))
                            if 0 <= new_j <= 4 and 0 <= new_k <= 4:
                                if places[i][new_j][new_k] == 'X':
                                    continue
                                elif places[i][new_j][new_k] == 'P':
                                    answer[i] = 0
                                    break
                            else:
                                continue
                    for l in range(4):
                        new_j, new_k = j + dx[l], k + dy[l]
                        if 0 <= new_j <= 4 and 0 <= new_k <= 4:
                            if places[i][new_j][new_k] == 'P':
                                answer[i] = 0
                                break
                        else:
                                continue

    return answer



places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))


"""
79 % 코드
def solution(places):
    answer = [1 for _ in range(5)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 좌상 우상 좌하 우하
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    for i in range(5):
        for j in range(5):
            for k in range(5):
                if places[i][j][k] != 'P':
                    continue
                else:
                    for l in range(4):
                        for m in range(2):
                            new_j, new_k = j + dr[l], k + dc[l]
                            if 0 <= new_j <= 4 and 0 <= new_k <= 4:
                                if places[i][new_j][new_k] == 'X':
                                    continue
                                elif places[i][new_j][new_k] == 'P':
                                    answer[i] = 0
                                    break
                            else:
                                continue
                    for m in range(4):
                        new_j, new_k = j + dr[m], k + dc[m]
                        if 0 <= new_j <= 4 and 0 <= new_k <= 4:
                            if places[i][new_j][new_k] == 'P':
                                answer[i] = 0
                                break

    return answer
"""