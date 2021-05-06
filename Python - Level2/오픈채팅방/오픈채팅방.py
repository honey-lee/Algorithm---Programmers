record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    n_record = [r.split() for r in record]
    nickname = {}
    ans = []
    for record in n_record:
        if len(record) == 3:
            nickname[record[1]] = record[2]

    for record in n_record:
        if record[0] == 'Enter':
            ans.append('{}님이 들어왔습니다.'.format(nickname[record[1]]))
        elif record[0] == 'Leave':
            ans.append('{}님이 나갔습니다.'.format(nickname[record[1]]))

    return ans

print(solution(record))