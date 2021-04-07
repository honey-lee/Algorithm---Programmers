array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    new_array = []
    answer = []
    for i in range(len(commands)):
        new_array = array[commands[i][0]-1:commands[i][1]]
        target = commands[i][2]-1
        new_array.sort()
        answer.append(new_array[target])

    return answer


print(solution(array, commands))
