def solution(skill, skill_trees):
    not_answer = 0
    n_skill = []
    for i in range(len(skill)):
        n_skill.append(skill[i])

    for j in range(len(skill_trees)):
        idx = 0
        for k in range(len(skill_trees[j])):
            if skill_trees[j][k] in n_skill:
                if n_skill[idx] != skill_trees[j][k]:
                    not_answer += 1
                    break
                else:
                    idx += 1
            else:
                continue

    return len(skill_trees) - not_answer



skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

print(solution(skill, skill_trees))

order = {0: 'C', 1: 'B', 2: 'D'}
print(order[1])