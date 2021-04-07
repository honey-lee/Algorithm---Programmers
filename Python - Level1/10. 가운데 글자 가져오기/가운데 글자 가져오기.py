s = 'abcde'

def solution(s):
    answer = ''
    len_s = len(s)

    if len_s % 2:
        answer = s[len_s // 2]
    else:
        answer = s[len_s // 2 - 1: len_s // 2 + 1]
    return answer


print(solution(s))


