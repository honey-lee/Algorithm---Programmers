"""
1 - 0001
2 - 0010
3 - 0011
4 - 0100
5 - 0101
6 - 0110
7 - 0111
8  - 1000
9 - 1001
10 - 1010
11 - 1011

짝수일 경우 1을 더하면 비트가 2개 이하로 다름

홀수 : 01로 끝나면
1을 더하면 10이니까 성립

11로 끝나면
(x + 2 ** (1의 갯수 - 1))

"""



def solution(number):
    result = []

    for i in range(2):
        if not number[i] % 2:
            result.append(number[i] + 1)
        else:
            if format(number[i], 'b').endswith('01'):
                result.append(number[i] + 1)
            elif format(number[i], 'b').endswith('11'):
                cnt = 0
                k = format(number[i], 'b')
                for j in range(len(k)-1, -1, -1):
                    if k[j] == '1':
                        cnt += 1
                    else:
                        break
                result.append(number[i] + 2 ** (cnt - 1))

    return result

numbers = [2,7]

print(solution(numbers))