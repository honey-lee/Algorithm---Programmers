priorities = [1, 1, 9, 1, 1, 1]
location = 0

def solution(priorities, location):
    n_priorities = []
    copied = 0

    for idx, priority in enumerate(priorities):
        n_priorities.append([idx, priority])

    priorities.sort(reverse=True)

    while n_priorities:
        while n_priorities[0][1] != max(priorities):
            t = n_priorities.pop(0)
            n_priorities.append(t)
        k = n_priorities.pop(0)
        copied += 1
        priorities.pop(0)
        if k[0] == location:
            break

    return copied


print(solution(priorities, location))