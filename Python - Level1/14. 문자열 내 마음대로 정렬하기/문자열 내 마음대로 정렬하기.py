strings = ['sun', 'bed', 'car']
n = 1

#아래와 같이 긴 코드를 작성하지 않고도 lambda함수를 사용해 정렬할 수 있다.
def solution(strings, n):
    #n값을 기준으로 정렬하되 n값이 같을 시 알파벳 순으로 정렬한다
    #따라서 우선 strings를 정렬한다
    #정렬된 strings 자체를 lambda함수를 활용해 n을 기준으로 다시 정렬한다.
    return sorted(sorted(strings), key=lambda strings: strings[n])

print(solution(strings, n))


"""
#문자 리스트 strings와 값n이 주어질때
# 각 문자열의 n번째에 위치한 알파벳을 기준으로 문자 리스트를 정렬하는 함수
def solution(strings, n):
    #바뀌어진 정답이 들어갈 리스트
    answer = []
    #n번째 문자들이 들어갈 리스트
    n_alpha = []

    #문자리스트에서 n번째 알파벳을 따로 떼서 n_alpha리스트에 넣고 정렬한다
    for string in strings:
        n_alpha.append(string[n])
    n_alpha.sort()

    #정렬되어 있는 기준 리스트를 고정하고
    for i in n_alpha:
        #정렬되어야 할 문자 리스트가 순회하다가
        for string in strings:
            #문자의 n번째 요소가 기준과 일치하면
            if string[n] == i:
                #정답리스트에 넣는다
                answer.append(string)
    #이 부분에서 오류발생!! 위와 같은 원리로 진행할 시 n_alpha에 동일한 알파벳이 있으면
    #단어들이 중복으로 들어간다

    #set로 변환해 중복을 제거하고 lambda를 활용해 n을 기준으로 정렬
    #이렇게 할 경우에 중복값이 없는 경우 위에서 한 정렬이 무의미해 틀린값이 나온다
    return sorted(set(answer), key = lambda x: string[n])
    #sorted(answer, key = lambda x: string[n])

"""
