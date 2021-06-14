"""
문제를 제대로 안읽어서 문제를 두번 푸는 동안 삽질을 했다....
문제의 조건은 무조건 0번 인덱스가 접두인 경우가 아닌 서로서로 접두가 되면 무조건 false 인것...
"""

def solution(phone_book):
    phone_book.sort()
    flag = True

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            flag = False
            return flag
    return flag

sample = ["12","123","1235","567","88"]


print(solution(sample))