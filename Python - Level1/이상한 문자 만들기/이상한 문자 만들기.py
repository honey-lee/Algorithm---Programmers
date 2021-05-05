

s = "try hello world"

def solution(s):
    answer = []
    s = s.split()
    for word in s:
        l = len(word)
        new_word = ''
        for i in range(l):
            if i % 2:
                new_word = new_word + word[i].lower()
            else:
                new_word = new_word + word[i].upper()

        answer.append(new_word)


    return ''.join(answer)


print(solution(s))

