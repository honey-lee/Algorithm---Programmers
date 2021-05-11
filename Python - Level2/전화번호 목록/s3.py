"""
문제를 제대로 안읽어서 문제를 두번 푸는 동안 삽질을 했다....
문제의 조건은 무조건 0번 인덱스가 접두인 경우가 아닌 서로서로 접두가 되면 무조건 false 인것...
"""

from collections import deque

def solution(phone_book):
    dq = deque()
    phone_book = sorted(phone_book, key = lambda x: len(x))
    dq.append(phone_book[-1])

    return dq

sample = ["119", "97674223", "1195524421"]


print(solution(sample))