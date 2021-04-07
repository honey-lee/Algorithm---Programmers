arr = [1,1,3,3,0,1,1]

# 연속된 숫자를 없애주는 함수를 정의
def solution(arr):
    # 연속된 숫자를 제거할 빈 리스트
    new_arr = []
    # 우선 빈 리스트에 기존 리스트의 0번 요소를 넣어준다.
    # 이 동작이 없으면 기존 리스트의 0, 1, -1번 요소가 같을 때 하나도 들어가지 않는다
    new_arr.append(arr[0]) #[1]
    # 기존 리스트의 범위 내에서
    for i in range(1, len(arr)):
        #기존 리스트의 요소와 그 전 요소가 같지 않은 경우 새 리스트에 넣음
        if arr[i] != arr[i-1]:
            new_arr.append(arr[i])
    return new_arr

print(solution(arr))
