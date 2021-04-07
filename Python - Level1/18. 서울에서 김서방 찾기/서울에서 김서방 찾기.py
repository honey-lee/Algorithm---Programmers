def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            location = i
    #return에도 f-string을 사용할 수 있다
    return '김서방은 {}에 있다'.format(location)