def solution(progresses, speeds):
    Q = []
    Q_compare = [i+1 for i in range(len(progresses))]
    min_value = min(Q_compare)
    done = False
    ans = []
    cnt = 0

    while not done:
        for idx, progress in enumerate(progresses):
            if progresses[idx] < 100:
                progresses[idx] += speeds[idx]
                if progresses[idx] >= 100:
                    Q.append(idx+1)
                    Q_compare[idx] = 101
                    cnt += 1
                if min_value in Q:
                    ans.append(cnt)
                    cnt = 0
                    min_value = min(Q_compare)
                if len(Q) == len(progresses):
                    done = True



    return ans



print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))