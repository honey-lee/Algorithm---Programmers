def solution(numbers):
    answer, i = 0, 0

    while i <= 9:
        if i not in numbers:
            answer += i
        i += 1

    return answer