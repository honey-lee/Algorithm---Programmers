def solution(m, n, puddles):
    way = [[1 for _ in range(m)] for _ in range(n)]

    for i, j in puddles:
        way[j - 1][i - 1] = 0

        # 모서리 부분이 침수되었을 때를 대비
        if i - 1 == 0:
            for a in range(j - 1, n):
                way[a][i - 1] = 0
        if j - 1 == 0:
            for b in range(i - 1, m):
                way[j - 1][b] = 0

    for i in range(1, n):
        for j in range(1, m):
            if way[i][j] != 0:
                way[i][j] = way[i - 1][j] + way[i][j - 1]


    return way[n - 1][m - 1] % 1000000007



m = 4
n = 3
puddles = [[2, 2]]

print(solution(m, n, puddles))


"""
1 1 1 1
1 0 1 1
1 1 1 1

"""