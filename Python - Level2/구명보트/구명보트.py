def solution(people, limit):
    ans = 0
    cnt = 0
    people.sort(reverse=True)

    while people:
        if people[0] + people[-1] <= limit:
            people.pop(0)
            people.pop(-1)
            cnt += 2
            ans += 1
        elif people[0] + people[-1] > limit:
            people.pop(0)
            cnt += 1
            ans += 1

    return ans


people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))

