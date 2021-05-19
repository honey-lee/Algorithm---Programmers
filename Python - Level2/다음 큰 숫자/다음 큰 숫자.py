from collections import Counter

def solution(n: int) -> int:
    flag = False
    # b_n = format(n, 'b')
    cnt_1 = Counter(format(n, 'b'))['1']

    while flag == False:
        n += 1
        if Counter(format(n, 'b'))['1'] == cnt_1:
            flag = True
            return n



print(solution(15))


