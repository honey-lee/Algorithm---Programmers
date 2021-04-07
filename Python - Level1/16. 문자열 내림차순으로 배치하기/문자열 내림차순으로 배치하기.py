s = "ZAbcdefg"


def solution(s):
    answer = sorted(s, reverse=True)
    tmp = []
    for i in range(len(answer)):
        if answer[i].isupper():
            tmp = answer[i:]
            answer = answer[:i]
            break
    tmp = sorted(tmp, reverse=True)
    answer.extend(tmp)
    return ''.join(answer)

print(solution(s))