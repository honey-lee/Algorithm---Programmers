n = 20
n2 = 4

def solution(n):

    # n이 짝수면 수박수박수박....
    if not n % 2:
        answer = '수박' * (n // 2)

    # n이 홀수면 수박수박수.....
    else:
        answer = '수' + ('박수' * (n // 2))

    return answer

print(solution(n))
print(solution(n2))
