"""
꼭 다시 풀어봐야할 DP 문제

"""
def solution(N, number):
    dp = []
    answer = 0

    for i in range(1, 9):
        all_case = set()
        check = int(str(N) * i)

        all_case.add(check)

        for j in range(i - 1):
            for op1 in dp[j]:
                for op2 in dp[-j - 1]:
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)

                    if op2 != 0:
                        all_case.add(op1 // op2)


        if number in all_case:
            answer = i
            break

        dp.append(all_case)


    return answer


N = 5
number = 12

print(solution(N, number))