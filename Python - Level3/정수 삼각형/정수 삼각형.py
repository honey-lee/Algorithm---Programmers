def solution(triangle):
    n = len(triangle)

    if n == 1:
        return triangle[0][0]

    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    return triangle[0][0]


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

print(solution(triangle))

"""
                7
            3       8
         8       1      0
       2    7       4     4
     4      5    2     6     5

"""

