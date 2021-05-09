def solution(n: int) -> list:
    return list(map(int, reversed(str(n))))



print(solution(12345))