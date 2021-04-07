# n = 8
# a = 4
# b = 7
#
#
# def fight(fight, a, b):
#     cnt = 1
#     while [a, b] not in fight:
#     # if [a, b] in fight:
#     #     return cnt
#     # else:
#         for i in fight:
#             if a == i[0] or b == i[0]:
#                 i.pop()
#             elif a == i[1] or b == [1]:
#                 i.pop(0)
#             else:
#                 i.pop()
#
#         for i in range(0, len(fight), 2):
#             fight.extend([fight[i] + fight[i+1]])
#
#         for i in fight:
#             if len(i) == 1:
#                 i.pop()
#         cnt += 1
#     return cnt
#
# def solution(n,a,b):
#     match = [(i+1) for i in range(n)]
#     fight = []
#     cnt = 1
#     for i in range(0, len(match), 2):
#         fight.append([match[i], match[i+1]])
#
#     fight(fight, a, b)
#
#     return fight
#
#
# print(solution(n, a, b))



list = [1, 2, 3]

print(1 in list)
print((1, 3) in list)
print(1, 2 in list)
print(3, 1 in list)