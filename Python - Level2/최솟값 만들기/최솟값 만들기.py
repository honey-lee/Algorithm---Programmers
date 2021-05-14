def solution(A, B):
    ans = 0
    A.sort()
    B.sort(reverse=True)

    for a, b in zip(A, B):
        ans += (a * b)

    return ans