def solution(m, n, puddles):
    answer = 0

    way = [[0 for _ in range(m)] for _ in range(n)]

    for i, j in puddles:
        way[i - 1][j - 1] = -1
        if not i - 1:
            for a in range(j - 1, m):
                way[j - 1][a] = -1
        elif not j - 1:
            for b in range(i - 1, n):
                way[i - 1][b] = -1

    for i in range(1, n):
        for j in range(1, m):
            if way[i][j] != -1:
                way[i][j] = way[i - 1][j] + way[i][j - 1]


    return way[n - 1][m - 1]



m = 4
n = 3
puddles = [[2, 2]]

print(solution(m, n, puddles))


"""

0 3 3 1
1 x 2 2
1 1 2 4


"""