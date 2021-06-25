"""
좌우조정 방법 수정
left, right 각각 1씩 늘려가며 문자 A가 아닌 문자에 먼저 도달하는 경우 찾기
left, right 중 더 짧은 거리의 위치로 이동하며 반복

"""

def solution(name):
    name = list(name)
    moves = [min(ord(s) - ord('A'), ord('Z') - ord(s) + 1) for s in name]

    answer = sum(moves)

    index = 0
    while True:
        left, right = 1, 1
        name[index] = 'A'

        if name == ["A"] * len(name): break

        for i in range(1, len(name)):
            if name[index + i] == "A": right += 1
            else: break

        for i in range(1, len(name)):
            if name[index - i] == "A": left += 1
            else: break

        if right > left:
            answer += left
            index -= left

        else:
            answer += right
            index += right
    return answer



name = "JEROEN"
name2 = "ABAAAAAAAAABB"
name3 = "ZZAAAZZ"

print(solution(name))
print(solution(name2))
print(solution(name3))