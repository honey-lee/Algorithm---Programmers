n = 5
lost = [2, 4]
reserve = [1, 3, 5]

def solution(n, lost, reserve):
    # 1. 수업을 들을 수 있도록 확정된 학생들
    # (체육복을 잃어버리지 않은 학생들)
    result = [i+1 for i in range(n) if i+1 not in lost]

    # 2. 체육복을 잃어버린 학생들 중에 수업을 들을 수 있는 학생들도 넣어주자

    # 체육복을 잃어버렸지만 여분 체육복이 있는 학생
    for stu in lost:
        if stu in reserve:
            result.append(stu)
            reserve.remove(stu)
    # 자신의 앞번호나 뒷번호에서 체육복을 빌릴 수 있는 학생
    for stu in lost:
        if stu-1 in reserve:
            result.append(stu)
            reserve.remove(stu - 1)
        elif stu+1 in reserve:
            result.append(stu)
            reserve.remove(stu + 1)


    return len(result)


print(solution(n, lost, reserve))