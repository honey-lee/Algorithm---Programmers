answers = [1, 2, 3, 4, 5]

def solution(answers):
    # 학생 1 이 문제를 찍는 방식
    a1 = [1, 2, 3, 4, 5]
    # 학생 2가 문제를 찍는 방식
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    # 학생 3이 문제를 찍는 방식
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 학생이 맞춘 문제의 갯수
    result = [0, 0, 0]

    # 최종 답
    ans = []

    # 정답의 길이
    k = len(answers)

    for i in range(k):
        s1 = i % len(a1)
        s2 = i % len(a2)
        s3 = i % len(a3)

        if a1[s1] == answers[i]:
            result[0] += 1
        if a2[s2] == answers[i]:
            result[1] += 1
        if a3[s3] == answers[i]:
            result[2] += 1

    for idx, answer in enumerate(result):
        if answer == max(result):
            ans.append(idx+1)
    return ans



print(solution(answers))





