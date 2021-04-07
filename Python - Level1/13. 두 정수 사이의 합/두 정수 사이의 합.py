a = 5
b = 3
# 두 수 사이의 모든 자연수를 더해주는 함수
def solution(a, b):
    # 수를 모두 더한 값을 담아줄 변수 total
    total = 0
    # 무조건 뒤에 작은 수가 오게 통일
    if a > b:
        a, b = b, a
        for i in range(a, b+1):
            total += i
        return total
    # 주어진 두 수가 같을 경우 그냥 리턴
    elif a == b:
        return a
    else :
        for i in range(a, b+1):
            total += i
        return total

print(solution(a, b))