
def solution(prices: list) -> list:
    answer = []
    stack = []
    for i in range(len(prices)):
        cnt = 0
        stack.append(prices[i])
        for j in range(i+1, len(prices)):
            cnt += 1
            if stack[-1] > prices[j]:
                break
        answer.append(cnt)

    return answer


print(solution([1, 2, 3, 2, 3]))