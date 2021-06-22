"""
가로 a, 세로 b 일때

a * b = brown + yellow
yellow = (a - 2) * (b - 2)
brown = (a + b - 2) * 2

=> 2a + 2b = brown + 4
=> 3a + 2b - ab = brown + 4
"""

import math

def solution(brown, yellow):
    ans = []
    # x = a + b
    x = int((brown + 4) / 2)

    tmp = []
    # 세로의 최소값이 3이니까 3부터 해서 더했을 때 x 가 되는 숫자들을 추려냄
    for i in range(x // 2 + 1, 3, -1):
        tmp.append([x - i, i])

    if math.sqrt(yellow) * 10 % 10 == 0.0:
        tmp.append([x // 2, x // 2])

    for i in range(len(tmp)):
        if (tmp[i][0] - 2) * (tmp[i][1] - 2) == yellow:
            ans.append(tmp[i][1])
            ans.append(tmp[i][0])
            break

    ans.sort(reverse=True)
    return ans

print(solution(10, 2))

print(math.sqrt(1) * 10 % 10)