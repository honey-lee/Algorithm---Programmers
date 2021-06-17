from math import gcd

def find_lcm(a, b):
    return a * b // gcd(a, b)


def solution(arr: list) -> int:
    arr.sort()

    if len(arr) == 1:
        return arr[0]

    elif len(arr) == 2:
        return (arr[0] * arr[1]) // gcd(arr[0], arr[1])


    else:
        a = arr[0]
        for i in arr[1:]:
            a = find_lcm(a, i)

    return a



arr = [2, 4, 6, 8, 10, 12, 14]



print(solution(arr))