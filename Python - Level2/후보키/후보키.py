from itertools import combinations
from collections import deque

def solution(relation):
    answer = 0
    # 학생 수
    row = len(relation)
    # 키의 갯수
    col = len(relation[0])

    candidates = []

    for i in range(1, col + 1):
        candidates.extend(combinations(range(col), i))

    unique = []
    for cand in candidates:
        tmp = [tuple([item[i] for i in cand]) for item in relation]
        if len(set(tmp)) == row:
            unique.append(cand)

    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            # 전체 다 겹치면 제거
            # discard 로 제거 시 index error 나지 않음
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
            ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))


