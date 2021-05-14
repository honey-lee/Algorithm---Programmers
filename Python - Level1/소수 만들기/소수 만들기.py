from itertools import combinations, combinations_with_replacement

# 소수 여부 판별하는 함수
def is_prime(num):
    cnt = 0
    for i in range(1, num+1):
        if not num % i:
            cnt += 1

    if cnt == 2:
        return True
    return False

def solution(nums):
    ans = 0
    new_nums = list(combinations(nums, 3))

    for numbers in new_nums:
        result = is_prime(sum(numbers))
        if result == True:
            ans += 1

    return ans
#
nums = [1, 2, 7, 6, 4]
#
# print(solution(nums))

test = list(combinations(nums, 3))
print(test)
print(len(test))

