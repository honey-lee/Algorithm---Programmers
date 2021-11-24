from itertools import permutations


def solution(k, dungeons):
    order = [i for i in range(len(dungeons))]
    n_order = []
    answer = -1
    for i in permutations(order, len(dungeons)):
        n_order.append(i)

    n_k = k
    for i in range(len(n_order)):
        tmp_answer = 0
        for j in range(len(n_order[i])):
            tar = n_order[i][j]
            if n_k >= dungeons[tar][0]:
                n_k -= dungeons[tar][1]
                tmp_answer += 1
            else:
                break
        if tmp_answer > answer:
            answer = tmp_answer
        n_k = k

