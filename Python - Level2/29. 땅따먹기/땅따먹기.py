from itertools import combinations

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

#i는 1씩 커지고 j는 가능한 조합들을 더해봄
#
def solution(land):
    column = list(combinations(([i for i in range(4)]), 3))
    row = [i for i in range(len(land))]
    max_value = -999

    for i in row:
        for j in column:
            tmp = 0
            for k in j:
                tmp += land[i][k]
                if tmp >= max_value:
                    max_value = tmp


    return max_value


# print(solution(land))


#
column = list(combinations(([i for i in range(4)]), 3))


