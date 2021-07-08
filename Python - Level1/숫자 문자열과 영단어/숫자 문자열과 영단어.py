def solution(s):
    answer = ''
    num_dict = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5,
                'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
    tmp = []


    for i in range(len(s)):
        if s[i].isnumeric():
            if not tmp:
                answer += s[i]
            if tmp:
                answer += str(num_dict[''.join(tmp)])
                tmp.clear()
                answer += s[i]
        elif s[i].isalpha():
            tmp.append(s[i])
            if len(tmp) >= 3:
                if ''.join(tmp) in num_dict:
                    answer += str(num_dict[''.join(tmp)])
                    tmp.clear()
                else:
                    continue

    if tmp:
        answer += str(num_dict[''.join(tmp)])





    return int(answer)



s = "one4seveneight"

print(solution(s))