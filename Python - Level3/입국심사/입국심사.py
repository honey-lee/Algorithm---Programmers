"""
최소, 최대범위를 구한 뒤 구하려고 하는 답은 이분탐색으로 범위를 좁혀가며 찾는 것

최대 범위는 심사관 중 가장 오래걸리는 심사관이 계속 심사하는 경우
최소, 최대 범위의 중간값인 mid가 n명을 심사할 수 있는지 아닌지 파악하며 이분 탐색

n명을 심사할 수 있다면 답을 갱신하고 최대 범위를 줄임
n명을 심사할 수 없다면 최소범위를 늘임
"""

def solution(n, times):
    answer = 0

    left = 1
    # 최대 범위
    right = n * max(times)

    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        for time in times:
            cnt += mid // time

            # 심사 인원수를 넘으면 다음 단계
            if cnt >= n:
                break

        if cnt >= n:
            answer = mid
            right = mid - 1

        elif cnt < n:
            left = mid + 1

    return answer


# n : 입국심사를 기다리는 사람 수
n = 6
# 심사에 걸리는 시간
times = [7, 10]

print(solution(n, times))
