'''
효율성 실패
'''

prices = [1, 2, 3, 2, 3, 1]
stack = []
top = -1

def push(item):
    global stack, top

    if top <= len(prices):
        # 가격이 유지된 시간, 주식 가격, 가격 끝 여부
        stack.append([0, item, 0])
        top += 1
        if len(stack) >= 2:
            for i in range(0, len(stack)-1):
                if stack[i][2]:
                    continue
                elif stack[-1][1] < stack[i][1]:
                    stack[i][0] += 1
                    stack[i][2] = 1
                elif stack[-1][1] >= stack[i][1] and not stack[i][2]:
                    stack[i][0] += 1

    return stack


def solution(prices):
    answer = []
    for i in range(len(prices)):
        push(prices[i])

    if len(stack) == len(prices):
        for i in range(len(prices)):
            answer.append(stack[i][0])

    return answer



print(solution(prices))





