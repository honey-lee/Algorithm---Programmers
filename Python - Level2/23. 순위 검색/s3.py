from itertools import combinations

def solution(info, query):
    answer = []
    info_dict = {}

    # for문을 이용해 요소 하나에 접근해서 list화 하는 방식
    for i in info:
        lis = i.split()
        # 코딩테스트 점수를 value 값으로
        info_key = lis[:-1]
        info_value = int(lis[-1])

        for j in range(5):
            for c in combinations(info_key, j):
                tmp_key = ''.join(c)
                if tmp_key in info_dict:
                    info_dict[tmp_key].append(info_value)
                else:
                    info_dict[tmp_key] = [info_value]

    # 오름차순 정렬
    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        qu = q.split()
        q_score = int(qu[-1])
        q_query = qu[:-1]

        while 'and' in q_query:
            q_query.remove('and')
        while '-' in q_query:
            q_query.remove('-')

        q_query = ''.join(q_query)

        if q_query in info_dict:
            scores = info_dict[q_query]
            if len(scores):
                s, e = 0, len(scores)
                while s < e:
                    mid = (s + e) // 2
                    if scores[mid] >= q_score:
                        e = mid
                    else:
                        s = mid + 1
                answer.append(len(scores) - s)
        else:
            answer.append(0)


    return answer

info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution(info, query))