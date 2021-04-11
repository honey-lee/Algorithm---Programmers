str1 = 'aaaa'
str2 = 'AAAA12'

# str1 = aa aa
# str2 = aa aa aa

print(str1.isalpha())

# 1. 문자열을 원하는 형태(다중집합)로 치환해주는 함수
def change_string(str):
    str_set = []
    # 문자열을 소문자 리스트로 만들어주고
    str = list(str.lower())

    # 전체 길이의 -1까지 두개씩 잘라서 준비해둔 str_set리스트에 넣어줌
    for i in range(0, len(str)-1):
        if str[i].isalpha() and str[i+1].isalpha():
            str_set.append(''.join([str[i], str[i+1]]))

    return str_set

# 2. 자카드 유사도를 검사하는 함수
def solution(str1, str2):
    # 두개의 문자열을 각각 두개씩 잘라서 다중집합으로 만들고
    str1_set = change_string(str1)
    str2_set = change_string(str2)
    # 결과
    result = 0

    # 2-1. 교집합 구하기
    #우선 두 다중함수 리스트에서 교집합을 구하고
    intersection = set(str1_set) & set(str2_set)
    #찐교집합의 갯수가 들어갈 리스트에
    intersection_final = []  #2
    for i in intersection:
        #두 개의 리스트에서 교집합요소의 갯수를 세서 작은 걸 넣고
        intersection_final.append(min(str1_set.count(i), str2_set.count(i)))

    # 2-2. 합집합 구하기
    union = set(str1_set) | set(str2_set)
    union_final = []
    # 위와 마찬가지로
    for i in union:
        # 이번에는 합집합 요소의 갯수를 세서 큰걸 넣음
        union_final.append(max(str1_set.count(i), str2_set.count(i))) #3

    try:
        # 자카드 유사도는 교집합 / 합집합
        result = sum(intersection_final) / sum(union_final)
    except:
        # zero divison 시 그냥 65536
        return 65536

    # 교집합이 없으면 0
    if result == 0:
        return 0
    # 이외에는 정수형태 * 655536
    return int(result * 65536)


print(solution(str1, str2))


"""
# 문자열을 원하는 형태로 치환해주는 함수
def change_string(str):
    str_set = []
    str = list(str.lower())

    for i in range(0, len(str)-1):
        if str[i].isalpha() and str[i+1].isalpha():
            str_set.append(''.join([str[i], str[i+1]]))

    return str_set


def solution(str1, str2):
    str1_set = change_string(str1)
    str2_set = change_string(str2)
    intersection = []
    result = 0

    for i in str1_set:
        if i in str2_set:
            intersection.append(i)
    intersection = list(set(intersection))

    union = str1_set + str2_set

    try:
        result = len(intersection) / len(union)
    except:
        pass

    if result == 0:
        return 65536
    return int(result * 65536)
"""