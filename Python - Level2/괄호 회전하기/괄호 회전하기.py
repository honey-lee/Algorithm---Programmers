def isright(s):
    stack = []
    k = len(s)

    for i in range(k):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        elif s[i] == ')':
            if not stack or stack[-1] != '(':
                return False
            else:
                stack.pop(-1)
        elif s[i] == '}':
            if not stack or stack[-1] != '{':
                return False
            else:
                stack.pop(-1)
        elif s[i] == ']':
            if not stack or stack[-1] != '[':
                return False
            else:
                stack.pop(-1)

    if stack:
        return False
    return True

def solution(s):
    answer = 0
    k = len(s)
    s = list(s)

    if isright(s):
        answer += 1

    for i in range(k-1):
        s.append(s.pop(0))
        if isright(s):
            answer += 1

    return answer


s = "[](){}"
print(solution(s))