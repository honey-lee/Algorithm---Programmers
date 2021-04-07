n = 12

def solution(n):
    division = [2, 3, 5, 7, 11]
    result = [0] * 5
    i = 0
    while n >= 1:
        if n % division[i] == 0:
            n /= 2
            result[i] += 1
            i += 1