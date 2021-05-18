def solution(s):
    ans = ''
    min = 99999
    max = -99999
    s = s.split()

    for i in range(len(s)):
        if int(s[i]) < min:
            min = int(s[i])
        if int(s[i]) > max:
            max = int(s[i])

    ans += str(min)
    ans += ' '
    ans += str(max)

    return ans




s = "-1 -2 -3 -4"
s2 = "1 2 3 4"

print(solution(s))
print(solution(s2))