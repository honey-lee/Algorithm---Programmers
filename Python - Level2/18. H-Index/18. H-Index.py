"""
H-index : 특정 연구원의 연구 성과를 평가하기 위한 지표, 발표한 논문수와 피인용수를 이용해 측정

논문중 피인용수가 많은 순서로 정렬해, 피인용수가 논문수와 같아지거나 피인용수가 논문수보다 작아지기 시작하는 숫자가
나의 H-index이다.

"""

citations = [3, 0, 6, 1, 5]

def solution(citations):
    ans = 0
    max_h = max(citations)

    for h in range(max_h, 0, -1):
        if len([i for i in citations if i >= h]) >= h:
            return h

    return ans



print(solution(citations))