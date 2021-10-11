def solution(weights, head2head):
    win_rate = []

    for i in range(len(head2head)):
        cnt = 0
        match = 0
        for j in range(len(head2head[i])):
            if head2head[i][j] == 'W' and weights[j] > weights[i]:
                cnt += 1
            if head2head[i][j] == 'W' or head2head[i][j] == 'L':
                match += 1
        if match != 0:
            win_rate.append([head2head[i].count('W') / match, cnt, weights[i], i + 1])
        else:
            win_rate.append([0, cnt, weights[i], i + 1])
    win_rate = sorted(win_rate, key=lambda x: (-x[0], -x[1], -x[2], x[3]))

    answer = [i[-1] for i in win_rate]

    return answer