def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        cnt = 0
        for j in range(1, i + 1):
            if not i % j:
                cnt += 1
        if not cnt % 2:
            answer += i
        elif cnt % 2:
            answer -= i

    return answer


left = 13
right = 17

print(solution(left, right))