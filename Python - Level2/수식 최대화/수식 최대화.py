from itertools import permutations
import copy

def solution(expression):
    ans = 0
    order = list(permutations(['+', '-', '*'], 3))
    stack = []
    tmp = ''
    expression1 = copy.deepcopy(expression)

    for i in range(len(expression)):
        if expression[i].isnumeric():
            tmp += expression[i]
        else:
            stack.append(int(tmp))
            stack.append(str(expression[i]))
            tmp = ''
    stack.append(tmp)

    expression1 = expression1.split('*')


    return expression1



expression = "100-200*300-500+20"
print(solution(expression))



