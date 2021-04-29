def solution(phone_number):
    answer = ''
    k = len(phone_number)
    right = phone_number[k - 4:k]

    if k == 4:
        return phone_number
    answer += '*' * (k-4)
    answer += right
    return answer

phone_number = "01033334444"

print(solution(phone_number))