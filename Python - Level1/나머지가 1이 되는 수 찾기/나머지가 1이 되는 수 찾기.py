def solution(n):
    answer = 1
    flag = False

    while not flag:
        if n % answer == 1:
            flag = True
        answer += 1

    return answer - 1

print(solution(12))