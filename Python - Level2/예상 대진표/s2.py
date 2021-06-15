def solution(n, a, b):
    ans = 0
    a += n - 1
    b += n - 1

    while a != b:
        a //= 2
        b //= 2
        ans += 1
    return ans

print(solution(8, 4, 7))