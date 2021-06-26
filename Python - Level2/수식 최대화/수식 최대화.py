from itertools import permutations
import copy

def solution(expression):
    ans = []
    # 연산자 적용 순서
    order = list(permutations(['+', '-', '*']))
    # 계산 대상 숫자
    nums = list(map(int, expression.replace('+', ' ').replace('-', ' ').replace('*', ' ').split(' ')))
    # 연산자들 (operator)
    op = []
    for i in range(len(expression)):
        if not expression[i].isnumeric():
            op.append(expression[i])

    while order:
        ans.append(calc(op, nums, order.pop(0)))

    return max(ans)

def calc(op, nums, op_):
    nums2 = copy.deepcopy(nums)
    op2 = copy.deepcopy(op)

    for i in op_:
        while i in op2:
            idx = op2.index(i)
            if i == '+':
                nums2[idx] = nums2[idx] + nums2[idx+1]
                nums2.pop(idx+1)
                op2.pop(idx)
            elif i == '-':
                nums2[idx] = nums2[idx] - nums2[idx+1]
                nums2.pop(idx + 1)
                op2.pop(idx)
            elif i == '*':
                nums2[idx] = nums2[idx] * nums2[idx+1]
                nums2.pop(idx + 1)
                op2.pop(idx)

    if nums2[0] >= 0:
        return nums2[0]
    return -nums2[0]



expression = "100-200*300-500+20"
print(solution(expression))



