def solution(n):
    ans = 0
    for i in range(1, n+1):
        if not n % i:
            ans += i
    return ans

print(solution(5))