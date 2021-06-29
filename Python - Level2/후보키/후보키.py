from itertools import combinations

def solution(relation):
    answer = 0
    idx = [i for i in range(4)]

    # 한개의 요소만으로 후보키가 될 수 있는 요소가 있는지 찾기

    for i in range(4):
        stack = []
        for j in range(len(relation)):
            if relation[j][i] not in stack:
                stack.append(relation[j][i])
            if len(stack) == len(relation):
                idx.remove(i)

    return idx


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],
            ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))