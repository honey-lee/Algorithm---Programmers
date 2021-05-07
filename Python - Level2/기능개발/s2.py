def solution(progresses, speeds):
    work_day = []
    i = 0
    j = 1
    ans = []

    for i in range(len(progresses)):
        work_day.append((100 - progresses[i]) * speeds[i])

    value = work_day[0]

    while sum(ans) <= len(progresses):
        while progresses[i] < value:
            i += 1
        ans.append(j)
        i += 1
        value = work_day[i]

    return work_day

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))