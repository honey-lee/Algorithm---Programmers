def solution(a, b):
    length = len(a)
    answer = 0

    for i in range(length):
        answer += (a[i] * b[i])

    return answer

a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]

print(solution(a, b))