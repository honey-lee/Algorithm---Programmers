from pandas import DataFrame as df

def solution(maps):
    m = len(maps)
    n = len(maps[0])

    start = [0, 0]

    game = [[0 for _ in range(n)] for _ in range(m)]

    return game

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]



print(df(maps))

print(solution(maps))