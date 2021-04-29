def solution(N, stages):
    players = len(stages)
    fail = [0] * N
    result = []
    real_result = []

    stages.sort()

    for i in range(1, N+1):
        try:
            rate = stages.count(i) / players
            fail[i-1] = rate
            players -= stages.count(i)
        except:
            pass

    for idx, fail in enumerate(fail):
        result.append([idx+1, fail])

    result = sorted(result, key = lambda x: x[1], reverse=True)

    for i in range(N):
        real_result.append(result[i][0])

    return real_result



N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))

