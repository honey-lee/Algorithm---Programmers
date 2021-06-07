from collections import deque

def solution(numbers, target):
    ans = 0
    # 현재의 합과 현재 인덱스
    Q = deque([[0, 0]])

    while Q:
        s, l = Q.popleft()
        if l > len(numbers):
            break
        elif l == len(numbers) and s == target:
            ans += 1
        Q.append([s + numbers[l-1], l+1])
        Q.append([s - numbers[l-1], l+1])

    return ans


numbers = [1, 1, 1, 1, 1]
target = 3

print(solution(numbers, target))