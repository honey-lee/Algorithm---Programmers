def solution(n, a, b):
    ans = 0
    flag = False
    fight = [i + 1 for i in range(n)]

    while not flag:
        stack = []
        ans += 1
        for i in range(0, len(fight), 2):
            if (fight[i], fight[i+1]) == (a, b) or (fight[i], fight[i+1]) == (b, a):
                flag = True
                return ans
            else:
                if fight[i] == a or fight[i] == b:
                    stack.append(fight[i])
                elif fight[i + 1] == a or fight[i + 1] == b:
                    stack.append(fight[i + 1])
                else:
                    stack.append(fight[i])

        fight = stack




print(solution(8, 4, 7))