"""
시간 초과
"""

def find_num(number):
    b_num = format(number, 'b')
    ans = 0

    i = 1
    while not ans:
        cnt = 0
        tmp_num = format(number + i, 'b')
        if len(b_num) == len(tmp_num):
            for j in range(len(b_num)):
                if b_num[j] != tmp_num[j]:
                    cnt += 1
            if cnt <= 2:
                ans = number + i
            i += 1
        elif len(b_num) > len(tmp_num):
            a = len(b_num) - len(tmp_num)
            n_tmp_num = '0' * a
            n_tmp_num += tmp_num

            for j in range(len(b_num)):
                if b_num[j] != n_tmp_num[j]:
                    cnt += 1
            if cnt <= 2:
                ans = number + i
            i += 1

        elif len(b_num) < len(tmp_num):
            a = len(tmp_num) - len(b_num)
            n_b_num = '0' * a
            n_b_num += b_num

            for j in range(len(n_b_num)):
                if n_b_num[j] != tmp_num[j]:
                    cnt += 1
            if cnt <= 2:
                ans = number + i
            i += 1

    return ans

def solution(numbers):
    answer = []

    for i in range(2):
        answer.append(find_num(numbers[i]))

    return answer

numbers = [2,7]

print(solution(numbers))


