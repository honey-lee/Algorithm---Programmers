def solution(dartResult):
    dart = []
    result = []
    score = {
        'S' : 1,
        'D' : 2,
        'T' : 3
    }

    i = len(dartResult) - 1
    j = i + 1
    while i >= 0:
        if dartResult[i].isdigit() and dartResult[i] != '0':
            dart.append(dartResult[i:j])
            j = i
            i -= 1
        elif dartResult[i] == '0':
            if i == 0:
                dart.append(dartResult[i:j])
                break
            elif dartResult[i-1] and dartResult[i-1].isdigit():
                i -= 1
                continue
            else:
                dart.append(dartResult[i:j])
                j = i
                i -= 1
        else:
            i -= 1

    dart.reverse()

    for k in range(3):
        if '10' not in dart[k]:
            ans = int(dart[k][0]) ** score[dart[k][1]]
            if len(dart[k]) == 3:
                if dart[k][2] == '#':
                    ans *= (-1)
                elif dart[k][2] == '*':
                    ans *= 2
                    if result:
                        result[-1] *= 2
            result.append(ans)

        else:
            ans = 10 ** score[dart[k][2]]
            if len(dart[k]) == 4:
                if dart[k][3] == '#':
                    ans *= (-1)
                elif dart[k][3] == '*':
                    ans *= 2
                    if result:
                        result[-1] *= 2
            result.append(ans)

    return sum(result)


# dartResult = '1S2D*3T'
# test = '1D#2S*3S'
#
# print(solution(dartResult))
# print(solution(test))
print(solution('0D2S#10S'))





