from pandas import DataFrame as df

def solution(rows, columns, queries):
    i = 1
    matrix = []
    ans = []


    for _ in range(rows):
        tmp = []
        for _ in range(columns):
            tmp.append(i)
            i += 1
        matrix.append(tmp)


    for x1, y1, x2, y2 in queries:
        # 최초의 숫자
        tmp = matrix[x1-1][y1-1]
        num = tmp

        # 우측으로 이동
        for k in range(x1-1, x2-1):
            t = matrix[k+1][y1-1]
            matrix[k][y1-1] = t
            num = min(t, num)

        # 아래로 이동
        for k in range(y1-1, y2-1):
            t = matrix[x2-1][k+1]
            matrix[x2-1][k] = t
            num = min(t, num)

        # 좌측으로 이동
        for k in range(x2-1, x1-1, -1):
            t = matrix[k-1][y2-1]
            matrix[k][y2-1] = t
            num = min(t, num)

        # 위로 이동 
        for k in range(y2-1, y1-1, -1):
            t = matrix[x1-1][k-1]
            matrix[x1-1][k] = t
            num = min(t, num)

        matrix[x1-1][y1] = tmp
        ans.append(num)

    return ans



rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

print(solution(rows, columns, queries))