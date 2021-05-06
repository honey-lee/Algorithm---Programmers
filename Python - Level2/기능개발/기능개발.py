def solution(progresses, speeds):
    Q = []
    done = False
    ans = []

    while not done:
        for idx, progress in enumerate(progresses):
            if progresses[idx] < 100:
                progresses[idx] += speeds[idx]
                if progresses[idx] >= 100:
                    Q.append(idx+1)
                if len(Q) == len(progresses):
                    done = True

    return Q



print(solution([93, 30, 55], [1, 30, 5]))