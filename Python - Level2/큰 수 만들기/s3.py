def solution(number, k):
    ans = []

    for idx, num in enumerate(number):
        while ans and ans[-1] < num and k > 0:
            ans.pop()
            k -= 1

        if k == 0:
            ans += number[idx:]
            break

        ans.append(num)

    if k > 0:
        ans = ans[:-k]

    return ''.join(ans)


print(solution("4177252841", 4))