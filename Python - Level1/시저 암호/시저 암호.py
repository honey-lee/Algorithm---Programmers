# 대문자 chr(65) ~ chr(90)
# 소문자 chr(97) ~ chr(122)

print(chr(97))

def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        elif 65 <= ord(s[i]) <= 90:
            if 65 <= ord(s[i]) + n <= 90:
                answer += chr(ord(s[i]) + n)
            else:
                answer += chr(65 + (ord(s[i]) + n - 90) - 1)

        elif 97 <= ord(s[i]) <= 122:
            if 97 <= ord(s[i]) + n <= 122:
                answer += chr(ord(s[i]) + n)
            else:
                answer += chr(97 + (ord(s[i]) + n - 122) - 1)

    return answer

print(solution('a B z', 4))