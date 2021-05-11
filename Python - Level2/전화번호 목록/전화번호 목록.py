"""
tc 3개 실패 및 효율성 2개 실패

"""
def solution(phone_book):
    answer = True
    prefix = phone_book[0]
    while ' ' in prefix:
        prefix = prefix.replace(' ', '')
    prefix_length = len(prefix)
    for i in range(1, len(phone_book)):
        while ' ' in phone_book[i]:
            phone_book[i] = phone_book[i].replace(' ', '')
        if len(phone_book[i]) >= prefix_length:
            if phone_book[i][:prefix_length] == prefix:
                answer = False
                return answer
    return answer


sample = ["11 9", "97674223", "11 95524421"]

print(solution(sample))