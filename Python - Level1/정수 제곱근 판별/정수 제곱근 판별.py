import math

def solution(n: int) -> int:

    return int(((math.sqrt(n)) + 1) ** 2) if not math.sqrt(n) * 10 % 10 else -1

print(solution(121))


