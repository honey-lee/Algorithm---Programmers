from pandas import DataFrame as df

def solution(w, h):
    ans = 0
    if w == h:
        return w * h - h

    elif w == 1 or h == 1:
        return 0

    for cur_w in range(0, w):
        y = h - ((h * cur_w) / w)
        if y % 1.0:
            ans += 1

    return w * h - ans - h



w = 8
h = 12
print(solution(w, h))