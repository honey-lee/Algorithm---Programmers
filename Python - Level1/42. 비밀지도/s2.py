def solution(n, arr1, arr2):
    n_arr1 = []
    n_arr2 = []
    result = []
    for num in arr1:
        bin = format(num, 'b')
        while len(bin) <= n-1:
            bin = '0' + bin
        n_arr1.append(bin)

    for num in arr2:
        bin = format(num, 'b')
        while len(bin) <= n - 1:
            bin = '0' + bin
        n_arr2.append(bin)

    for i in range(len(arr1)):
        new_num = ''
        for j in range(n):
            if n_arr1[i][j] == '1' or n_arr2[i][j] == '1':
                new_num += '#'
            else:
                new_num += ' '
        result.append(new_num)

    return result





n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

print(solution(n, arr1, arr2))

