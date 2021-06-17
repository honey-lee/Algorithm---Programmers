"""
가로 or 세로 1이라면 다 잘리기 때문에 0
가로 == 세로면 딱 한 변의 길이 만큼만 잘림


가로 줄을 기준으로 볼 때
사각형이 1개잘리거나 2개잘리거나 이다. 3개잘리는 경우는 never

가로 x 세로 = 짝 x 짝 이고 4보다 클 경우
1 2 1 1 2 1 순서로 잘림

가로 x 세로 = 짝 x 홀 일 경우 세로가 짝수면 중심에서 가로 2개걸리고 지나감

정리해보면
w x h에서 w, h를 빼고 gcd(w, h)를 다시 더한만큼이 망가짐

"""
from math import gcd

def solution(w, h):
    if w == h:
        return w * h - h

    elif w == 1 or h == 1:
        return 0

    else:
        return w * h - (w + h - gcd(w, h))



w = 8
h = 12
print(solution(w, h))