def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

price = 3
money = 20
count = 4

print(solution(price, money, count))