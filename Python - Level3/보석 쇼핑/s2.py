# 슬라이딩 윈도우

def solution(gems):
    answer = []
    gems_set = set(gems)

    count_dict = {}
    count_set = set()

    # 현재 구간
    s, e = 0, 0

    finals, finale = 0, 0
    finding = 0
    length = 987654321

    for s in range(len(gems)):
        flag = False

        for e in range(finding, len(gems)):
            # 아직 딕셔너리에 없다면 추가
            if gems[e] not in count_dict.keys():
                count_dict[gems[e]] = 1
                count_set.add(gems[e])
            # 이미 들어있다면 value값 1 더하기
            else:
                count_dict[gems[e]] += 1

            # 모든 종류의 보석이 다 들어왔으면
            if len(count_set) == len(gems_set):
                # 가장 짧은 구간 저장
                if (e - s) < length:
                    length = e - s
                    finals = s
                    finale = e

                flag = True
                finding = e
                break

        if not finding:
            break

        if gems[s] in count_dict.keys():
            if count_dict[gems[s]] == 1:
                del count_dict[gems[s]]
                count_set.remove(gems[s])
            else:
                count_dict[gems[s]] -= 1

        if gems[finding] in count_dict.keys():
            if count_dict[gems[finding]] == 1:
                del count_dict[gems[finding]]
                count_set.remove(gems[finding])
            else:
                count_dict[gems[finding]] -= 1

    return [finals + 1, finale + 1]




gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

print(solution(gems))


print(abs(3.5))