citations = [3, 0, 6, 1, 5]

def solution(citations):
    # 전체 작성된 논문의 갯수
    n = len(citations)
    # H index 지수, 최대값이 전체 논문의 수와 같다
    h = len(citations)
    # 인용된 횟수를 오름차순으로 정렬
    citations.sort()
    cnt_h = 0

    if h != 0:
        for citation in citations:
            if citation >= h:
                cnt_h +=1
            else:
                continue

            if cnt_h == h:
                break
            else:
                h -= 1

    return h



print(solution(citations))