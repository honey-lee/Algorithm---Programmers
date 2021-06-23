def convert(p):
    u = ''
    v = ''
    stack = ''
    left = 0
    right = 0
    for i in range(len(p)):
        if stack == 0:
            v += p[i]
            if stack and left and right and left == right:
                u = stack
                stack = 0
        elif p[i] == '(':
            stack += p[i]
            left += 1
            if stack and left and right and left == right:
                u = stack
                stack = 0
        elif p[i] == ')':
            stack += p[i]
            right += 1
            if stack and left and right and left == right:
                u = stack
                stack = 0

    return u, v

def isbalanced(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            if not stack:
                return False
            if stack:
                stack.pop(-1)
    if stack:
        return False
    return True

def change(s):
    new_s = ''

    if len(s) <= 2:
        return ''

    for i in range(1, len(s)-1):
        if s[i] == '(':
            new_s += ')'
        elif s[i] == ')':
            new_s += '('

    return new_s

def solution(p):

    if not len(p):
        return p

    u, v = convert(p)

    if isbalanced(u) == True:
        return u + solution(v)

    elif isbalanced(u) == False:
        new_u = change(u)



        return '(' + solution(v) + ')' + new_u

    return solution(p)


p = "()))((()"

print(solution(p))

