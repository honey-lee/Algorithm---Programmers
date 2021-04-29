def lotto(lottos, win_nums):
    rank = 1
    lottos.sort()
    win_nums.sort()

    if lottos == win_nums:
        return rank
    else:
        same_num = 0
        for j in lottos:
            if j in win_nums:
                same_num += 1

    if same_num == 5:
        rank = 2
        return rank
    elif same_num == 4:
        return 3
    elif same_num == 3:
        return 4
    elif same_num == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    answer = []
    best, worst = 0, 0
    if not lottos.count(0):
        best = worst = lotto(lottos, win_nums)
        answer.append(best)
        answer.append(worst)

    else:
        worst = lotto(lottos, win_nums)
        while lottos and not lottos[0]:
            lottos.pop(0)

        for j in win_nums:
            if j not in lottos:
                lottos.append(j)
            if len(lottos) == 6:
                break

        best = lotto(lottos, win_nums)
        answer.append(best)
        answer.append(worst)

    return answer

lottos = [1, 2, 0, 0, 0, 0]
win_nums = [1, 2, 3, 4, 5, 6]

print(solution(lottos, win_nums))



