numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

numbers2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand2 = 'left'

def solution(numbers, hand):
    # 결과값
    result = []
    # 숫자간의 절대값 차이가 작을 수록 이동거리 짧음
    # 왼손 오른손 각 위치
    l_location, r_location = 0, 0

    for number in numbers:
        if number == 1 or number == 4 or number == 7:
            result.append('L')
            l_location = number
        elif number == 3 or number == 6 or number == 9:
            result.append('R')
            r_location = number
        elif number == 2 or number == 5 or number == 8 or number == 0:
            # 위치가 같으면
            if abs(l_location - number) == abs(r_location - number):
                if hand == 'right':
                    result.append('R')
                    r_location = number
                else:
                    result.append('L')
                    l_location = number
            elif abs(l_location - number) < abs(r_location - number):
                result.append('L')
                l_location = number
            else:
                result.append('R')
                r_location = number

    return ''.join(result)

print(solution(numbers, hand))
print(solution(numbers2, hand2))


# 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
# 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #