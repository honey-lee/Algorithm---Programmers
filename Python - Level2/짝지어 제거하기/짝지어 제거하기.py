"""
시간 초과
"""

def check(s):
    chr = ''
    flag = False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            flag = True
            chr = s[i]
            break

    s = s.replace(chr, '', 2)

    return flag, s

def solution(s):
    while check(s)[0] == True:
        s = check(s)[1]
        if not len(s):
            return 1

    return 0