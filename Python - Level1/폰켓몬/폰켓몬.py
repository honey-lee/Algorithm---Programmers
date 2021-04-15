nums = [3, 1, 2, 3]
nums2 = [3, 3, 3, 2, 2, 4]
nums3 = [3, 3, 3, 2, 2, 2]

def solution(nums):
    k = len(nums)
    answer = []

    nums_set = set(nums)

    for i in nums_set:
        if len(answer) < k//2:
            answer.append(i)

    return len(answer)


print(solution(nums))
print(solution(nums2))
print(solution(nums3))