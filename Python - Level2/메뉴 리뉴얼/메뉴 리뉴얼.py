"""
문제를 잘 읽자......!
"""

from itertools import combinations
from collections import Counter

def find_max(menus: list) -> str:
    counter = Counter(menus).most_common()
    max_count = counter[0][1]
    max_menu = []

    if max_count >= 2:
        for c in counter:
            if c[1] == max_count:
                max_menu.append(c[0])
            else:
                break

    return max_menu

def solution(orders: list, course: list) -> list:
    n_orders = []
    for order in orders:
        n_orders.append(sorted(order))
    ans = []
    result = []
    for j in course:
        tmp = []
        for i in range(len(n_orders)):
            tmp2 = combinations(n_orders[i], j)
            for k in tmp2:
                tmp.append(k)
        if tmp:
            ans.append(find_max(tmp))

    for i in ans:
        for j in i:
            result.append(''.join(j))

    return sorted(result)




orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]

print(solution(orders, course))