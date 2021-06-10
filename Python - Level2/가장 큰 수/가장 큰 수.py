"""
lambda 함수를 사용해 문자열을 각 3번씩 반복했을때 큰것 순으로 정렬한다
x * 3을 하는 이유? 인수값이 1000이하니까 3자리수로 맞춘뒤 비교하는 것
문자열 비교는 ASCII 값으로 치환되어 정렬된다.
666 101010 222 가 있을 때 첫번째 인덱스 값으로 비교한다
6 = 86 / 1 = 81 / 2 = 82

"""


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

numbers = [3, 30, 34, 5, 9]

print(solution(numbers))

print('999' < '343434')