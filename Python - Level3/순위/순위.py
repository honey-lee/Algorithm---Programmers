# 딕셔너리 써보기
from collections import defaultdict

def solution(n, results):
    answer = 0

    # 누가 누굴 이기고 누가 누구한테 졌는지
    wins = defaultdict(set)
    loses = defaultdict(set)

    for i, j in results:
        wins[i].add(j)
        loses[j].add(i)

    for i in range(n + 1):
        # 합집합 구하기
        for loser in wins[i]:
            loses[loser] |= loses[i]

        for winner in loses[i]:
            wins[winner] |= wins[i]

    for i in range(n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

print(solution(n, results))


"""
4 3
4 2 
3 2def solution(n, results):
    answer = 0
    draw = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(len(results)):
        a = 0
        b = -1
        flag = False
        while not flag:
            tmp = 0
            if not draw[[i][0]][b]:
                draw[[i][0]][b] = results[i][1] 
                tmp += 1
            elif draw[[i][0]][b]:
                b -= 1
            if not draw[[i][1]][a]:
                draw[[i][1]][a] = results[i][0]
                tmp += 1
            elif draw[[i][1]][a]:
                a += 1
            if tmp == 2:
                flag = True
            
            
    return draw


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

print(solution(n, results))
1 2
2 5 

4 3 1 2 5


"""