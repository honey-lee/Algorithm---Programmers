"""
단어별로 짝/홀수 인덱스를 판단해야함
"""

def solution(s):
    ans = ''
    s = s.split()

    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == ' ':
                ans += ' '
            elif j % 2:
                ans += s[i][j].lower()
            elif not j % 2:
                ans += s[i][j].upper()
        if i != len(s) - 1:
            ans += ' '

    return ans

print(solution("try hello world"))

s = "try hello world"

print(s.split())