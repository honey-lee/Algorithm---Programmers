# 그리디
def solution(d, budget):
    ans = 0
    d.sort()

    while budget > 0 and d:
        budget -= d[0]
        d.pop(0)
        ans += 1

    if budget < 0:
        ans -= 1

    return ans



d = [1, 3, 2, 5, 4]
budget = 9

print(solution(d, budget))