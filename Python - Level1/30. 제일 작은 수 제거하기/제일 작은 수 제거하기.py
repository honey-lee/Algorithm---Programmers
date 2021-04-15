arr = [1, 4, 3, 2, 1, 1, 1]
arr2 = [10]

def solution(arr):
    min_num = min(arr)
    arr.remove(min_num)

    if len(arr) == 0:
        arr.append(-1)

    return arr


print(solution(arr))
print(solution(arr2))

def solution2(arr):
    for i in arr:
        if i == min(arr):
            arr.remove(i)

    if len(arr) == 0:
        arr.append(-1)

    return arr

print(solution2(arr))

'''
실패한 순회 코드 (일부 코드 실패)
수 하나를 없애고 나면 두번째로 작았던 수가 min값이 되서 또 없어지기 때문에??

def solution(arr):
    for i in arr:
        if i == min(arr):
            arr.remove(i)

    if len(arr) == 0:
        arr.append(-1)

    return arr
'''