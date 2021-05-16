from itertools import combinations

def solution(number, k):
    idx = list(combinations([i for i in range(len(number))], len(number) - k))
    ans = 0

    for i in range(len(idx)):
        tmp = ''
        for j in range(len(idx[i])):
            tmp += number[idx[i][j]]
        if int(tmp) > ans:
            ans = int(tmp)

    return str(ans)


print(solution('1231234', 3))


