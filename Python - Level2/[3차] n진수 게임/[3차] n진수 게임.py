"""
n : 진법, t : 미리 구할 숫자의 갯수, m : 인원, p : 튜브의 순서

10 ~ 15 : A ~ F
"""
from collections import deque
import string

Q = deque()

def convert(num, base):
    # 전체 숫자와 알파벳
    tmp = string.digits + string.ascii_uppercase
    # 몫과 나머지를 구함
    q, r = divmod(num, base)

    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]

def convert_q(num):
    global Q

    for i in range(len(num)):
        Q.append(num[i])


def solution(n, t, m, p):
    answer = ''
    num = 0
    global Q

    while len(Q) <= m * t:
        tmp = str(convert(num, n))
        convert_q(tmp)
        num += 1

    while len(answer) < t:
        answer += Q[p-1]
        p += m


    return answer


# print(convert(15, 2))
# print(convert_q(str(1111)))
print(solution(2, 4, 2, 1))