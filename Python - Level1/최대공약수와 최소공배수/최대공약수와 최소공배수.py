import math


def solution(n, m: int) -> list:
    a = math.gcd(n, m)
    b = int((n * m) / a)

    return [a, b]


print(solution(3, 12))