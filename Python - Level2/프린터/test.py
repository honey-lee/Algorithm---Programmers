sample = [5, 7, 2, 12, 9]

def sorting(list):
    tmp = 0
    for i in range(len(list) - 1):
        for j in range(len(list) - 2 - i):
            if list[j] > list [j + 1]:
                tmp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tmp

    return list

print(sorting(sample))