from pandas import DataFrame as df

def solution(n):
    answer = []
    square = []
    nums = sum([i for i in range(1, n + 1)])

    # 하 우 좌상
    dr = [1, 0, -1]
    dc = [0, 1, -1]

    for i in range(n):
        tmp = [0 for _ in range(i + 1)]
        square.append(tmp)


    square[0][0] = 1
    m = 1
    r, c = 0, 0

    while m < nums:
        for i in range(3):
            r += dr[i]
            c += dc[i]
            while 0 <= r < n and 0 <= c <= len(square[r - 1]) and not square[r][c]:
                m += 1
                square[r][c] = m
                r += dr[i]
                c += dc[i]
            r -= dr[i]
            c -= dc[i]

    for i in range(len(square)):
        for j in range(len(square[i])):
            answer.append(square[i][j])

    return answer

n = 4
print(solution(n))