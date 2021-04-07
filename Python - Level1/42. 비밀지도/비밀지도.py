from pandas import DataFrame as df
n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

def solution(n, arr1, arr2):
    for i in range(len(arr1)):
        arr1[i] = bin(arr1[i])


for i in range(len(arr1)):
    arr1[i] = bin(arr1[i])

print(arr1)




"""
46(2) = 011110
27(2) = 011011

map = [0 for _ in range(n)]
    ans = []

    for i in range(n):
        #or 연산
        map[i] = arr1[i] | arr2[i]

    for i in range(n):
        x = 1 << n | map[i]

    return map

print(solution(n, arr1, arr2))

"""


