str1 = 'aa1+aa2'
str2 = 'AAAA12'

# str1 = aa aa
# str2 = aa aa aa

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
    # 결과
    result = 0

    #교집합
    intersection = set(str1_set) & set(str2_set)
    intersection_final = []
    for i in intersection:
        intersection_final.append(min(str1_set.count(i), str2_set.count(i)))

    #합집합
    union = set(str1_set) | set(str2_set)

    union_final = []
    for i in union:
        union_final.append(max(str1_set.count(i), str2_set.count(i)))


    try:
        result = sum(intersection_final) / sum(union_final)
    except:
        return 65536

    if result == 0:
        return 0
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