def solution(n):
    ans = 0

    while n != 0:
        if not n % 2:
            n /= 2
        else:
            n -= 1
            ans += 1

    return ans

n = 5

print(solution(5000))