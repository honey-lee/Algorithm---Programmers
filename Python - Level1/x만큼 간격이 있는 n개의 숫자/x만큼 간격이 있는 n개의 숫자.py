def solution(x, n : int) -> list:
    answer = []
    y = x
    for i in range(n):
        answer.append(x)
        x += y

    return answer

print(solution(2, 5))