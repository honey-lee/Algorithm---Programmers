from pandas import DataFrame as df

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

# def solution(info, query):
answer = [0] * len(query)

#info와 query의 정보를 모두 공백 단위로 쪼개서 2차원 배열에 넣어준다
new_info = []
new_query = []

for i in range(len(info)):
    new_info.append(info[i].split())

for j in range(len(query)):
    new_query.append(query[j].split())

# query의 정보를 중심으로 해서 탐색하면서 4개의 단어가 부합하고
# info의 점수가 더 높으면 조건에 부합하는 지원자이다
# query에 -가 있을 경우 무조건 1점씩 준다
# 총 5점을 받으면 합격이다


for j in range(len(new_query)):
    for i in new_info:
        cnt = 0
        # 우선 -는 무조건 1점이니까 점수로 더해주고
        cnt += new_query[j].count('-')
        for n in i:
            if n in new_query[j]:
                cnt += 1
            elif n.isdigit():
                if n >= new_query[j][-1]:
                    cnt += 1
            else:
                continue

            if cnt == 5:
                answer[j] += 1
                break

print(answer)



