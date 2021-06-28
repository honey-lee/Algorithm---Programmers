"""
경우의 수 : 모자, 안경, 코트 가 있을 경우
(모자 갯수 + 1)(안경 갯수 + 1)(코트 갯수 + 1) - 1

각 종류의 옷의 갯수와 / 해당 종류의 옷을 입지않을 수도 있으니 +1을 해서 곱한다.
아무것도 안입는 경우는 없으니 -1한다

"""
def solution(clothes):
    my_clothes = {}
    answer = 1

    for clothe in clothes:
        key = clothe[1]
        value = clothe[0]
        if key in my_clothes:
            my_clothes[key].append(value)
        else:
            my_clothes[key] = [value]

    for key in my_clothes.keys():
        answer *= (len(my_clothes[key]) + 1)

    answer -= 1

    return answer



clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))