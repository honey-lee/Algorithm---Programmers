def solution(x):
    n_x = str(x)
    n_num = 0
    for i in range(len(n_x)):
        n_num += int(n_x[i])
    if x % n_num:
        return False
    return True


print(solution(12))