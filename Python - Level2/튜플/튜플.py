from collections import Counter

def solution(s):
    tmp = ''
    stack = []
    ans = []

    for i in range(len(s)):
        if s[i].isnumeric():
            tmp += s[i]
        else:
            if tmp:
                stack.append(int(tmp))
                tmp = ''

    tmp2 = Counter(stack).most_common()

    for i in range(len(tmp2)):
        ans.append(tmp2[i][0])

    return ans

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s2 = "{{20,111},{111}}"

# print(s, type(s))
# print(s.split(','))

print(solution(s))
print(solution(s2))