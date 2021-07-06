"""
다익스트라 거리 계산 문제
"""

from collections import deque

def bfs(s, G, K, N):
    Q = deque([s])
    T = [999999] * (N + 1)
    T[1] = 0

    while Q:
        s, cost = Q.popleft()

        for i in G[s]:
            e, n_cost = i[0], i[1]

            if cost + n_cost <= K and cost + n_cost < T[e]:
                T[e] = cost + n_cost
                Q.append([e, cost + n_cost])

    return T

def solution(N, road, K):
    answer = 0

    G = [[] for _ in range(N + 1)]

    # 출발점, 도착점, 비용
    for s, e, cost in road:
        G[s].append([e, cost])
        G[e].append([s, cost])

    lst = bfs([1, 0], G, K, N)
    for i in lst:
        if i != 999999:
            answer += 1

    return answer



N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

print(solution(N, road, K))
