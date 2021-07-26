def solution(n, edge):
    adj = [[] for _ in range(n + 1)]
    dist = [0] * (n + 1)

    for e1, e2 in edge:
        adj[e1].append(e2)
        adj[e2].append(e1)

    queue = [[1, 0]]

    while queue:
        idx, depth = queue.pop(0)
        dist[idx] = depth
        for i in adj[idx]:
            if not dist[i]:
                dist[i] = 1
                queue.append([i, depth + 1])
        depth += 1


    dist[1] = 0

    return dist.count(max(dist))

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


print(solution(n, edge))