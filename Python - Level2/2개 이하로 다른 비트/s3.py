def solution(numbers):
    result = []

    for number in numbers:
        if not number % 2:
            result.append(number + 1)
        else:
            binary_num = bin(number)[2:]
            binary_num = "0" + binary_num
            one_idx = binary_num.rfind("0")
            binary_num = list(binary_num)
            binary_num[one_idx] = "1"
            binary_num[one_idx + 1] = "0"
            result.append(int("".join(binary_num), 2))

    return result