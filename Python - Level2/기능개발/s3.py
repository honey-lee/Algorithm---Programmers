import math

def solution(progresses, speeds):
    num = math.ceil((100 - progresses[0]) / speeds[0])

    ans = [0]

    for i, j in zip(progresses, speeds):
        if num >= math.ceil((100 - i) / j):
            ans.append(ans.pop() + 1)
        elif num < math.ceil((100 - i) / j):
            num = math.ceil((100 - i) / j)
            ans.append(1)

    return ans


progresses = [95, 90, 99, 99, 80, 99]
speeds = 	[1, 1, 1, 1, 1, 1]


print(solution(progresses, speeds))