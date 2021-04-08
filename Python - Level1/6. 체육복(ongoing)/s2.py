n = 5
lost = [1, 2, 3]
reserve = [2, 3, 4]

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
    # 중요!!!
    # 이 부분이 없어서 로직이 안돌아갔는데
    # 우선 체육복을 잃어버렸어도 수업을 들을 수 있게 되었으면 잃어버린 목록에서도
    # 없애줘야 아래의 연산이 제대로 된다
    tmp = []
    for stu in lost:
        if stu in result:
            tmp.append(stu)
    for stu in tmp:
        if stu in lost:
            lost.remove(stu)

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