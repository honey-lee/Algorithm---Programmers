"""
대각선 자리에 대한 예외처리 실패

대각선이라도 칸막이 있으면 거리두기 한것으로 봐야함
"""


def solution(places):
    answer = [1 for _ in range(5)]

    # 좌상 우상 좌하 우하
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(5):
        for j in range(5):
            for k in range(5):
                if places[i][j][k] != 'P':
                    continue
                else:
                    for l in range(4):
                        new_j, new_k = j + dx[l], k + dy[l]
                        if 0 <= new_j <= 4 and 0 <= new_k <= 4:
                            if places[i][new_j][new_k] == 'P':
                                if l == 0:
                                    if places[i][j-1][k] != 'X' or places[i][j][k-1] != 'X':
                                        answer[i] = 0
                                        break
                                if l == 1:
                                    if places[i][j-1][k] != 'X' or places[i][j][k+1] != 'X':
                                        answer[i] = 0
                                        break
                                if l == 2:
                                    if places[i][j][k-1] != 'X' or places[i][j+1][k] != 'X':
                                        answer[i] = 0
                                        break
                                if l == 3:
                                    if places[i][j][k+1] != 'X' or places[i][j+1][k] != 'X':
                                        answer[i] = 0
                                        break
                        else:
                                continue
                    for m in range(4):
                        for n in range(2):
                            new_j, new_k = j + (dr[m] * (n + 1)), k + (dc[m] * (n + 1))
                            if 0 <= new_j <= 4 and 0 <= new_k <= 4:
                                if places[i][new_j][new_k] == 'X':
                                    break
                                elif places[i][new_j][new_k] == 'P':
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