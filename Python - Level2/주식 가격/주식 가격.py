prices = [1, 2, 3, 2, 3, 1]

"""
효율성 실패
"""

def solution(prices):
    answer = [i for i in range(len(prices)-1, -1, -1)]

    for i in range(len(prices)):
        if prices[i] == min(prices[i:]):
            continue
        else:
            n_prices = prices[i:]
            for j in range(len(n_prices)):
                if n_prices[j] < prices[i]:
                    answer[i] = j
                    break

    return answer

print(solution(prices))






