def solution(n):
    ans = ''
    tmp = []
    n_str = str(n)
    for i in range(len(n_str)):
        tmp.append(int(n_str[i]))
    tmp.sort(reverse=True)

    for num in tmp:
        ans += str(num)

    return int(ans)


print(solution(118372))
