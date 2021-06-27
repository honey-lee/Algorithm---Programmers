def solution(s):
    answer = ''

    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        elif answer and answer[-1] == ' ':
            answer += s[i].upper()
        elif answer and answer[-1].isalpha() and s[i].isalpha():
            answer += s[i].lower()
        elif not answer and s[i].isalpha():
            answer += s[i].upper()
        else:
            answer += s[i]

    return answer

s = "3people     unFollowed me"
s2 = " i can d o i t "

print(solution(s))
print(solution(s2))

if s2[-1] == ' ':
    print('yes')
else:
    print('no')