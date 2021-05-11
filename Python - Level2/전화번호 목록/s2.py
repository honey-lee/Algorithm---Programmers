def solution(phone_book):
    prefix = phone_book[0]
    prefix_length = len(phone_book[0])
    for i in range(1, len(phone_book)):
        if len(phone_book[i]) >= prefix_length:
            phone_book[i] = phone_book[i][:prefix_length]
        else:
            continue

    if phone_book.count(prefix) >= 2:
        return False
    return True


sample = ["119", "97674223", "1195524421"]

print(solution(sample))