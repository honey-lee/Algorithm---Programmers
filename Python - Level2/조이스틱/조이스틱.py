"""
A - 65
M - 77
N - 78
O - 79
Z - 90

A ~ N 까지는 13번 움직여야함
A ~ O 까지 14번
A ~ Z ~ O : 12
A ~ Z ~ N : 13

즉, N까지는 정방향, O부터는 역방향으로 움직이는게 조작이 빠르다

좌우 조정 시 마지막 엣지케이스 발생
"""

def solution(name: str) -> int:
    moves = []
    move_cnt = list(filter(lambda x: name[x] != 'A', range(1, len(name))))

    for i in range(len(name)):
        if ord(name[i]) - 65 <= 13:
            moves.append(ord(name[i]) - 65)
        else:
            moves.append(90 - ord(name[i]) + 1)

    ans = sum(moves)

    move = min(max(move_cnt), len(name) - min(move_cnt))


    return move


name = "JEROEN"
name2 = "ABAAAAAAAAABB"
name3 = "ZZAAAZZ"

print(solution(name))
print(solution(name2))
print(solution(name3))

