def solution(n):
    ans = 0
    ls = list(str(n))
    for num in ls:
        ans += int(num)

    return ans