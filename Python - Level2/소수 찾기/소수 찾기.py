"""
2개 시간초과
"""

from itertools import permutations

def is_prime(num):
    cnt = 0
    for i in range(1, num + 1):
        if not num % i:
            cnt += 1

    if cnt == 2:
        return True
    return False

def solution(numbers):
    ans = 0
    tmp = []
    tmp2 = []
    num_list = []
    for i in range(len(numbers)):
        tmp.append(numbers[i])

    for i in range(1, len(numbers)+1):
        tmp2.append(list(permutations(tmp, i)))

    for i in range(len(tmp2)):
        for j in range(len(tmp2[i])):
            if int(''.join(tmp2[i][j])) not in num_list:
                num_list.append(int(''.join(tmp2[i][j])))

    for i in range(len(num_list)):
        if is_prime(num_list[i]):
            ans += 1

    return ans


numbers = '17'


print(solution('17'))