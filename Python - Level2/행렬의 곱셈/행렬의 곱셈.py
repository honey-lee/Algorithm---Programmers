"""
https://mathbang.net/562
행렬의 곱셈

0행 x 0열
1행 x 1열
"""

def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        tmp_list = []
        for j in range(len(arr2[0])):
            tmp = 0
            for k in range(len(arr2)):
                tmp += arr1[i][k] * arr2[k][j]
            tmp_list.append(tmp)
        answer.append(tmp_list)


    return answer



arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = 	[[3, 3], [3, 3]]

print(solution(arr1, arr2))


"""
1 4            3 3
3 2            3 3
4 1


0,0 x 0,0 + 0,1 x 1,0
0,0 x 1,0 + 0,1 x 1,1

1,0 x 0,0 + 1,1 x 1,0
1,0 x 1,0 + 1,1 x 1,1

2,0 x 0,0 + 2,1 x 1,0
2,0 x 1,0 + 2,1 x 1,1

"""