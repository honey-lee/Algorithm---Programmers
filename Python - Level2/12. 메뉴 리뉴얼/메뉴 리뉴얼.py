from itertools import combinations
from collections import defaultdict, Counter

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]


def solution(orders, course):
    counter = defaultdict(int)
    max_count = defaultdict(int)
    answer = []


    for i in orders:
        for j in course:
            if len(i) < j:
                continue
            else:
                new_menu = combinations(i, j)
                for menu in new_menu:
                    food = ''.join(menu)
                    counter[food] += 1
                    if max_count[j] < counter[food]:
                        max_count[j] = counter[food]

    for c in course:
        if max_count[c] < 2:
            continue

        answer += [i[0] for i in Counter.items() if len(i[0]) == c and i[1] == max_count(c)]


    return sorted(answer)

print(solution(orders, course))

