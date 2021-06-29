"""
통과는 했지만 words의 길이가 n의 배수가 아닐경우 index out of range 발생하여
edge case 있을 수 있는 코드 

"""

def solution(n, words):
    stack = []
    cnt = 1
    answer = []

    for i in range(0, len(words), n):
        for j in range(i, i + n):
            if not stack:
                stack.append(words[j])
            elif stack and words[j] not in stack and stack[-1][-1] == words[j][0]:
                stack.append(words[j])
            else:
                answer.append(j % n + 1)
                answer.append(cnt)
                return answer
        cnt += 1

    if not answer:
        answer.append(0)
        answer.append(0)

    return answer


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

m = 3
words2 = ["tank", "kick", "know", "wheel", "land"]

print(solution(n, words))
