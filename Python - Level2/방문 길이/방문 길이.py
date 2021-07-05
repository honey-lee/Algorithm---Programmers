from pandas import DataFrame as df

def solution(dirs):
    move = set()
    start = (0 , 0)

    # UDLR
    dr = {'U' : 0, 'D' : 0, 'L' : -1, 'R' : 1}
    dc = {'U' : -1, 'D' : 1, 'L' : 0, 'R' : 0}

    for dir in dirs:
        r, c = start
        new_r = r + dr[dir]
        new_c = c + dc[dir]

        if -5 <= new_r <= 5 and -5 <= new_c <= 5:
            m = tuple(sorted([(r, c), (new_r, new_c)]))
            move.add(m)
            start = (new_r, new_c)


    return len(move)


dirs = "ULURRDLLU"

print(solution(dirs))

