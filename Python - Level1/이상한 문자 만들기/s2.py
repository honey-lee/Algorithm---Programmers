"""
18.8점 나오는 코드...
이유를 모르겠음
"""


def solution(s):
    ans = ''
    for i in range(len(s)):
        if s[i] == ' ':
            ans += ' '
        elif i % 2:
            ans += s[i].lower()
        elif not i % 2:
            ans += s[i].upper()


    return ans



