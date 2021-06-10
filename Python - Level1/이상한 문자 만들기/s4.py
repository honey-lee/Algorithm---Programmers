"""
드디어 드디어 통과한 코드!!!!!!
공백이 여러개 연속 있을 때를 감안하지 못해서 계속 헤맸다...
당연히 문자열 사이에 공백을 한칸으로 생각하고 split() 도구를 계속 사용했던게 원인..
"""
def solution(s):
    ans = ''

    for i in range(len(s)):
        if s[i] == ' ':
            ans += ' '
        elif s[i].isalpha():
            if not ans or not ans[-1].isalpha():
                ans += s[i].upper()
            elif ans[-1].isalpha() and ans[-1].islower():
                ans += s[i].upper()
            elif ans[-1].isalpha() and ans[-1].isupper():
                ans += s[i].lower()

    return ans


s = "try hello world"

print(solution(s))

