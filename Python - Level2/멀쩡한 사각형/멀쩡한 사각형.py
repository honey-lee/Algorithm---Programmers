from pandas import DataFrame as df

def solution(w, h):
    square = [[0 for _ in range(w)] for _ in range(h)]

    return df(square)



w = 8
h = 12
print(solution(w, h))