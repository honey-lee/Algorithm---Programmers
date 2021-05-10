"""
stack
"""

def solution(s):
    stack = [s[0]]

    for i in range(1, len(s)):
        if not stack:
            stack.append(s[i])
        elif stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])


    return 1 if not stack else 0


print(solution('baabaa'))

