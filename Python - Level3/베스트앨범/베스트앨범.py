def solution(genres, plays):
    answer = []
    genre_times = {}

    for i in range(len(genres)):
        if genres[i] not in genre_times:
            genre_times[genres[i]] = plays[i]
        else:
            genre_times[genres[i]] += plays[i]

    genre_times = sorted(genre_times.items(), key=lambda x: x[1], reverse=True)

    for i in range(len(genre_times)):
        if genres.count(genre_times[i][0]) == 1:
            answer.append(genres.index(genre_times[i][0]))



    return answer


genres = ["classic", "pop", "classic", "classic", "pop", "a"]
plays = [500, 600, 150, 800, 2500, 200]

print(solution(genres, plays))