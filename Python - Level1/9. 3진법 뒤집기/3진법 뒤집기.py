n = 45

# 1. 10진법 -> 3진법
def decimal_to_ternary(num):
    number = []
    while num > 0:
        number = [num % 3] + number
        num //= 3

    return number

# 2. 3진법 -> 10진법
def ternary_to_decimal(num):
    answer = 0
    for i in range(len(num)):
        answer += num[i] * (3 ** (len(num)-1-i))

    return answer

def solution(n):
    # 10진법을 3진법으로
    number = decimal_to_ternary(n)
    # 앞뒤 반전
    number.reverse()
    # 3진법을 10진법으로
    number = ternary_to_decimal(number)

    return number

print(solution(n))