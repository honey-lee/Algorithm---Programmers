def solution(n, computers):
    answer = 0
    adj = [[] for _ in range(n)]
    visited = [0] * n

    for i in range(len(computers)):
        for j in range(n):
            if computers[i][j] and i != j:
                adj[i].append(j)

    for i in range(n):
        if not visited[i]:
            answer += 1
            queue = [i]
            visited[i] = True

            while queue:
                t = queue.pop(0)
                for j in adj[t]:
                    if not visited[j]:
                        visited[j] = True
                        queue.append(j)


    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

print(solution(n, computers))