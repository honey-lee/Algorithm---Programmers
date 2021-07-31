def solution(gems):
    # 진열된 갯수
    total_cnt = len(gems)
    # 보석의 종류 갯수
    gems_kind = len(set(gems))
    answer = []
    buy = []
    final_buy = []

    cnt = 0

    for i in range(total_cnt):
        if gems[i] not in buy:
            cnt += 1
        buy.append(gems[i])
        if cnt == gems_kind:
            buy.append(i + 1)
            break

    answer.append(buy.pop())
    cnt = 0

    for i in range(len(buy)-1, -1, -1):
        if buy[i] not in final_buy:
            cnt += 1
        final_buy.append(buy[i])
        if cnt == gems_kind:
            answer.append(i + 1)
            break

    answer.sort()

    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

print(solution(gems))


"""
dia ruby ruby dia dia emerald saphire

saphire emerald dia dia ruby

"""