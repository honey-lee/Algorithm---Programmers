"""
효율성 실패
"""

def solution(info, query):
    answer = []
    info_ = ''
    query_ = ''
    for i in range(len(info)):
        info_ += info[i]
        info_ += ' '

    info_ = info_.split()

    for j in range(len(query)):
        query_ += query[j]
        query_ += ' '

    query_ = query_.split()

    while 'and' in query_:
        query_.remove('and')

    for i in range(0, len(query_), 5):
        cnt = 0
        for j in range(0, len(info_), 5):
            if int(query_[i + 4]) <= int(info_[j + 4]):
                if query_[i] == '-' or query_[i] == info_[j]:
                    if query_[i + 1] == '-' or query_[i + 1] == info_[j + 1]:
                        if query_[i + 2] == '-' or query_[i + 2] == info_[j + 2]:
                            if query_[i + 3] == '-' or query_[i + 3] == info_[j + 3]:
                                cnt += 1
        answer.append(cnt)



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