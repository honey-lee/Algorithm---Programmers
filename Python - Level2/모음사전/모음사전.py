def solution(word):
    cal_dict = {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5}
    nums = [5 ** i for i in range(1, 6)]
    max_num = sum(nums)
    ans = 0

    for i in range(len(word)):
        ans += (max_num // nums[i]) * cal_dict[word[i]]

    return ans

# A 1 ~ 781
# E 782 ~ 1562
# I 1563 ~ 2343
# O 2344 ~ 3124
# U 3125 ~ 3905

# 5  25  125  625  3125
# 3905 // 5, 3905 // 25, ....