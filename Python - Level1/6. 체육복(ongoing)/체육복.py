n = 5
lost = [2, 4]
reserve = [1, 3, 5]


def solution(n, lost, reserve):
    ans = n
    #체육복을 잃어버린 학생이 없으면 모두 수업을 듣고 끝난다
    if len(lost) == 0:
        return ans
    #체육복을 잃어버린 학생이 있을 때는 우선 수업을 들을 수 있는 학생수를 뺀다
    else:
        ans - len(lost)
        for i in lost:
            if i-1 or i+1 in reserve:
                ans += 1
                reserve.pop()

"""
#n 학생의 수, lost 체육복을 도난당한 학생, reserve 여벌 체육복이 있는 학생
def solution(n, lost, reserve):
    answer = 0
    # 전체 학생 수 n에서 도난당한 학생 수를 빼고 answer에 더한다. 우선 확실히 참여 가능한 학생 수
    answer += (n - len(lost))
    # 우선 여벌 체육복이 있는데 도난당한 학생이 있는 경우 빌려줄 수 없으므로 reserve에서 제거한다
    for j in reserve:
        if j in lost:
            reserve.remove(j)
            lost.remove(j)
            answer += 1

    # 그리고 참여하지 못하는 학생 중에 체육복을 빌릴 수 있는 학생도 더한다
    for i in lost:
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
        elif i+1 in reserve:
            answer += 1
            reserve.remove(i+1)
        else:
            continue
    return answer

print(solution(n, lost, reserve))
"""
