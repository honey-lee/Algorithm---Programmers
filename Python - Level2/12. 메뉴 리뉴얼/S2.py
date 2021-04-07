from itertools import combinations
from collections import defaultdict, Counter

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]


def solution(orders, course):
    tmp = []
    tmp2 = []
    course_combination = [[] for _ in range(len(course))]

    for i in orders:
        for j in course:
            if len(i) < j:
                continue
            else:
                tmp.append(combinations(i, j))

    for i in tmp:
        for j in i:
            tmp2.append(''.join(j))

    for i in tmp2:
        for j in course:
            if len(i) == j:
                course_combination[]


print(solution(orders, course))




