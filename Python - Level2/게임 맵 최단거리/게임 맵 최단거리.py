from pandas import DataFrame as df
from collections import deque

def solution(maps):
    # 가로 n, 세로 m
    n = len(maps[0])
    m = len(maps)
    queue = deque([(0, 0)])

    if n == 1 or m == 1:
        for i in range(m):
            for j in range(n):
                if maps[i][j] == 0:
                    return -1
        if n == 1:
            return m
        elif m == 1:
            return n

    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    visited = [[0 for _ in range(n)] for _ in range(m)]
    visited[0][0] = 1

    while queue:
        cur_r, cur_c = queue.popleft()
        if cur_r == m-1 and cur_c == n-1:
            return visited
        for i in range(4):
            n_r = cur_r + dr[i]
            n_c = cur_c + dc[i]
            if 0 <= n_r < m and 0 <= n_c < n and not visited[n_r][n_c] and maps[cur_r][cur_c] == 1:
                visited[n_r][n_c] = visited[cur_r][cur_c] + 1
                queue.append((n_r, n_c))
    return -1



maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps2 = [[1, 1, 1, 1, 1]]


# print(df(maps))

print(solution(maps))
print(solution(maps2))