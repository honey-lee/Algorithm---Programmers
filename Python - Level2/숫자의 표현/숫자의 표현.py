

def solution(n):
    answer = 0

    my_list = [i+1 for i in range(n)]

    for i in range(len(my_list)):
        tmp = 0
        j = 0
        while tmp < n:
            tmp += my_list[i + j]
            j += 1
        if tmp == n:
            answer += 1

    return answer


n = 15

print(solution(n))