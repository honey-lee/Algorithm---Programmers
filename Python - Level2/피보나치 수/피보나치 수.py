"""
(A + B) % C = ((A % C) + (B % C)) % C

int 자료형은 -2,147,483,648 ~ 2,147,483,647 까지의 값만을 표현할 수 있음
총 숫자 갯수 2 ** 32, 1바이트는 8비트니까

프로그래밍을 할 때 정수의 범위에 신경을 쓰는 것이 중요

"""

def solution(n):

    ans = []

    for i in range(n + 1):
        if i == 0 or i == 1:
            ans.append(i)
        else:
            a = ans[i-1] + ans[i-2]
            ans.append(a % 1234567)

    return ans[-1]


"""
a b
0 1
1 1
1 2
2 3
3 4
"""