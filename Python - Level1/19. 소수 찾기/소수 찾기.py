n = 10

def solution(n):
    # 2부터 n+1까지의 집합
    num = set(range(2, n+1))

    # 2부터 n까지 반복문을 돌리며
    for i in range(2, n+1):
        # i가 num안에 있다면
        if i in num:
            # i의 배수는 num집합에서 제외
            num -= set(range(2*i, n+1, i))
    return list(num)


print(solution(n))