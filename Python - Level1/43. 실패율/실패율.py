N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def sub(n):
    return int(n * 100000)

def solution(N, stages):
    fail = []
    failure_rate = []
    answer = []
    #게임을 한 사람의 수
    k = len(stages)

    for i in range(1, N + 1):
        fail.append(stages.count(i))

    for i in range(len(fail)):
        failure_rate.append(fail[i] / k)
        k -= fail[i]

    failure_rate = list((idx + 1, failure_rate) for idx, failure_rate in enumerate(failure_rate))

    failure_rate = sorted(failure_rate, key=lambda x: x[1], reverse=True)

    for i in range(len(failure_rate)):
        answer.append(failure_rate[i][0])

    return answer


print(solution(N, stages))





"""
def sub(n):
    return int(n * 100000)

def solution(N, stages):
    #각 단계별로 멈춰있는 인원을 계산할 빈 리스트
    fail = []
    failure_rate = []
    answer = []
    k = len(stages)
    #1부터 N+1단계까지 멈춰있는 인원을 세서 넣는다
    #N+1단계일 경우 모두 통과한 사람
    for i in range(1, N+1):
        fail.append(stages.count(i))

    for i in range(len(fail)):
        failure_rate.append(fail[i] / k)
        k -= fail[i]

    failure_rate = list(map(sub, failure_rate))

    failure_rate = list((idx + 1, failure_rate) for idx, failure_rate in enumerate(failure_rate))

    failure_rate = sorted(failure_rate, key=lambda x: x[1], reverse=True)

    for i in range(len(failure_rate)):
        answer.append(failure_rate[i][0])

    return answer



print(solution(N, stages))
"""