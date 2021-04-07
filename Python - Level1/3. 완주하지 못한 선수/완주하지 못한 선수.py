participant = ['leo', 'kiki', 'eden']
completion = ['kiki', 'eden']

def solution(participant, completion):
    #참여 선수 정렬
    participant.sort()
    #완주 선수 정렬
    completion.sort()
    
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

print(solution(participant, completion))