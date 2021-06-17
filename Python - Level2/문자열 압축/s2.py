def solution(s: str) -> int:
    k = len(s)
    ans = 1001

    if k == 1:
        return 1

    for i in range(1, k // 2 + 1):
        new_s = ''
        stack = []
        stack.append(s[:i])
        for j in range(i, k, i):
            if new_s and new_s[0].isalpha():
                new_s += s[j:j + i]

            if not stack:
                if len(s[j:j + i]) == i:
                    stack.append(s[j:j + i])
                else:
                    new_s += s[j:j + i]
            else:
                if stack[-1] == s[j:j + i]:
                    stack.append(s[j:j + i])
                else:
                    if len(stack) != 1:
                        new_s += str(len(stack))
                    new_s += stack[0]
                    stack.clear()
                    if len(s[j:j + i]) == i:
                        stack.append(s[j:j + i])
                    else:
                        new_s += s[j:j + i]

        if stack:
            if len(stack) != 1:
                new_s += str(len(stack))
            new_s += stack[0]

        if len(new_s) <= ans:
            ans = len(new_s)

    return ans


s = "aabbaccc"

print(solution(s))