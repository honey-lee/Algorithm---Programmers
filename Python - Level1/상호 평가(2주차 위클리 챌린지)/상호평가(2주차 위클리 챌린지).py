def solution(scores):
    answer = ''

    k = len(scores)

    n_scores = list(map(list, zip(*scores)))

    for i in range(k):
        if max(n_scores[i]) == n_scores[i][i]:
            if n_scores[i].count(max(n_scores[i])) == 1:
                n_scores[i][i] = 0
        elif min(n_scores[i]) == n_scores[i][i]:
            if n_scores[i].count(min(n_scores[i])) == 1:
                n_scores[i][i] = 0

    for i in range(k):
        if not n_scores[i].count(0):
            avg = sum(n_scores[i]) / k
            if avg >= 90:
                answer += 'A'
            elif avg >= 80:
                answer += 'B'
            elif avg >= 70:
                answer += 'C'
            elif avg >= 50:
                answer += 'D'
            else:
                answer += 'F'
        else:
            avg = sum(n_scores[i]) / (k - 1)
            if avg >= 90:
                answer += 'A'
            elif avg >= 80:
                answer += 'B'
            elif avg >= 70:
                answer += 'C'
            elif avg >= 50:
                answer += 'D'
            else:
                answer += 'F'

    return answer


scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]

print(solution(scores))