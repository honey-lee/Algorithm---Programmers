def solution(gems):
    answer = []
    shortest = 987654321
    s, e = 0, 0

    # 보석의 종류 갯수
    gems_kind = len(set(gems))

    count_dict = {}

    while e < len(gems):
        if gems[e] not in count_dict:
            count_dict[gems[e]] = 1
        else:
            count_dict[gems[e]] += 1

        e += 1

        if len(count_dict) == gems_kind:
            while s < e:
                if count_dict[gems[s]] > 1:
                    count_dict[gems[s]] -= 1
                    s += 1

                elif shortest > e - s:
                    shortest = e - s
                    answer = [s + 1, e]
                    break

                else:
                    break

    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

print(solution(gems))


list = [1, 2, 3, 4]
print(list[-1:])
print(list[1:])
