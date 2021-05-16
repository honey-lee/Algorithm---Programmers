from itertools import combinations

def solution(number, k):
    nums = []
    numbers = list(combinations(number, len(number) - k))
    for i in range(len(numbers)):
        nums.append(int(''.join(numbers[i])))
    return str(max(nums))


number = "1924"
k = 2

print(solution(number, k))


"""
1231234

"""