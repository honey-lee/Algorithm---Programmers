def solution(s):
    stack = []

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if not stack:
                return False
            stack.pop(-1)

    if stack:
        return False

    return True

print(solution('(())()'))