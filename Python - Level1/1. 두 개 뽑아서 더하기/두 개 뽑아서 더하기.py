def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in numbers[i+1:]:
            s = numbers[i] + j
            if s not in answer:
                answer.append(s)
    answer.sort()
    return answer


numbers = [2, 1, 3, 4, 1]

print(solution(numbers))