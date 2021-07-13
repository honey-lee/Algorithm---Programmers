"""
A - 65
Z - 90

"""

def solution(msg):
    answer = []
    cha_dict = {}

    # A ~ Z 딕셔너리 우선 생성
    for i in range(26):
        cha_dict[chr(65 + i)] = i + 1

    i, j = 0, 0

    while True:
        j += 1
        if j == len(msg):
            answer.append(cha_dict[msg[i : j]])
            break
        if msg[i : j + 1] not in cha_dict:
            cha_dict[msg[i : j + 1]] = len(cha_dict) + 1
            answer.append(cha_dict[msg[i : j]])
            i = j

    return answer

msg = "KAKAO"
print(solution(msg))