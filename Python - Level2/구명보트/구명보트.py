def solution(people, limit):
    ans = 0
    people.sort()

    left = 0
    right = len(people) - 1

    while left < right:
        if people[left] + people[right] <= limit:
            ans += 1
            left += 1
            right -= 1
        else:
            ans += 1
            right -= 1
    if left == right:
        ans += 1


    return ans


people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))

