def solution(n, left, right):
    answer = []
    cnt = 1
    for i in range(n):
        for j in range(1, n + 1):
            if cnt <= j:
                answer.append(j)
            else:
                answer.append(cnt)
        cnt += 1

    return answer[left:right + 1]