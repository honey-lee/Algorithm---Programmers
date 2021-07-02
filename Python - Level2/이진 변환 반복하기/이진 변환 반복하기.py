def solution(s):
    answer = []
    zero_cnt, cnt = 0, 0
    flag = False

    while not flag:
        if s == '1':
            flag = True
            break
        l = 0
        for i in range(len(s)):
            if s[i] == '1':
                l += 1
            else:
                zero_cnt += 1

        s = format(l, 'b')
        cnt += 1

    answer.append(cnt)
    answer.append(zero_cnt)


    return answer


s = "110010101001"

print(solution(s))