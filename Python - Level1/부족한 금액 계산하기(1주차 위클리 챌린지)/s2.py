def solution(price, money, count):

    while count:
        money -= price * count
        count -= 1

    if money >= 0:
        return 0
    return -money



price = 3
money = 20
count = 4

print(solution(price, money, 1))