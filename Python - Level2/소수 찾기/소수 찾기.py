"""
2개 시간초과
"""

from itertools import permutations

def is_prime(num):
    cnt = 0

    for i in range(1, num + 1):
        if not num % i:
            cnt += 1

        """
        cnt가 3을 넘을 경우 소수일수없기 때문에
        이 부분이 없으면 tc 2개 시간 초과
        """
        if cnt >= 3:
            return False

    if cnt == 2:
        return True
    return False

def solution(numbers):
    ans = 0
    num_list = []
    for i in range(1, len(numbers)+1):
        num_list = num_list + list(permutations(list(numbers), i))

    for i in range(len(num_list)):
        num_list[i] = int(''.join(num_list[i]))

    for i in set(num_list):
        if is_prime(i):
            ans += 1

    return ans


numbers = '17'


print(solution('17'))