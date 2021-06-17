# def solution(s: str) -> int:
#     k = len(s)
#     ans = 1001
#     my_s = []
#
#     if k == 1:
#         return 1
#
#     for i in range(k):
#         my_s.append(s[i])
#
#     for i in range(1, k // 2):
#         new_s = ''
#         tmp = ''
#         stack = []
#         for j in range(i):
#             tmp += my_s.pop(j)
#         stack.append(tmp)
#
#         while my_s:
#             if stack:
#                 if my_s[:i] == stack[-1]:
#                     for j in range(i):
#                         tmp += my_s.pop(j)
#                     stack.append(tmp)
#                 else:
#                     new_s += str(len(stack))
#                     new_s += stack[0]
#                     stack.clear()
#                     for j in range(i):
#                         tmp += my_s.pop(j)
#                     stack.append(tmp)
#             if not stack:
#                 if len(my_s) >= i:
#                     for j in range(i):
#                         tmp += my_s.pop(j)
#                 else:
#                     while my_s:
#                         new_s += my_s.pop(0)
#
#         if len(new_s) <= ans:
#             ans = len(new_s)
#
#     return ans


s = "aabbaccc"

my_s = ['a']

print(my_s[:1]==s[:1])
print(str(my_s[:1]))
print(s[:1])
# print(solution(s))
