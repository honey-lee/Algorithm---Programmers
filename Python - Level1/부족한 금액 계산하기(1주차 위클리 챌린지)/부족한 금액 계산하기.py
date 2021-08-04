def solution(price, money, count):
    total_price = 0

    for i in range(1, count + 1):
        total_price += price * i

    if total_price <= money:
        return 1
    else:
        return total_price - money



price = 3
money = 20
count = 4

print(solution(price, money, count))