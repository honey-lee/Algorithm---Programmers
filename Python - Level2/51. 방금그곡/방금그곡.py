# 기억한 멜로디 m
m = "ABCDEFG"
# 재생시간 HH:MM, 노래 제목, 노래의 멜로디
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]


# 1. 전체 길이를 일치화 하기 위해 #이 있을 경우 소문자로 바꿔줌
def remove(s):
    s = s.replace('C#', 'c')
    s = s.replace('D#', 'd')
    s = s.replace('F#', 'f')
    s = s.replace('G#', 'g')
    s = s.replace('A#', 'a')

    return s

# 2. 노래의 재생시간 계산
def calculate_time(list):
    start_time1 = list[0].split(',')[0].split(':')
    end_time1 = list[0].split(',')[1].split(':')
    start_time2 = list[1].split(',')[0].split(':')
    end_time2 = list[1].split(',')[1].split(':')`

    play_hour1 = int(end_time1[0]) - int(start_time1[0])
    play_hour2 = int(end_time2[0]) - int(start_time2[0])

    if play_hour1 == 0:
        total1 = int(end_time1[1]) - int(start_time1[1])
    else:
        total1 = 60 * play_hour1 + int(end_time1[1]) - int(start_time1[1])

    if play_hour2 == 0:
        total2 = int(end_time2[1]) - int(start_time2[1])
    else:
        total2 = 60 * play_hour2 + int(end_time2[1]) - int(start_time2[1])

    return total1, total2

# 3. 재생중이었던 노래를 찾기 위한 함수
def solution(m, musicinfos):
    m = remove(m)
    play_time = calculate_time(musicinfos)
    for idx, musicinfo in enumerate(musicinfos):
        musicinfo = remove(musicinfo)
        musicinfo = musicinfo.split(',')

    if play_time[0] == len(musicinfo[3]):
        melody1 = musicinfo[3]
    elif play_time[0] > len(musicinfo[3]):
        melody1 = musicinfo[3] + musicinfo[3][:play_time[0]]
    else:
        melody1 = musicinfo[3][:play_time[0]]


    return melody1

print(solution(m, musicinfos))


a = 'abcde'

a = a.replace('a', 'aa').replace('b', 'bb')
print(a)


# def solution(m, musicinfos):
#     for idx, musicinfo in enumerate(musicinfos):
#         # 위에서 만들어둔 길이 일치 함수를 사용함
#         remove(m)
#         for idx, musicinfo in enumerate(musicinfos):
#             musicinfo = remove(musicinfo)
#             musicinfo = musicinfo.split(',')
#
#
#     return musicinfo[1].split(':')
#
# print(solution(m, musicinfos))

"""
def changecode(music_): 
    music_ = music_.replace('C#', 'c')
    music_ = music_.replace('D#', 'd')
    music_ = music_.replace('F#', 'f')
    music_ = music_.replace('G#', 'g')
    music_ = music_.replace('A#', 'a')    
    return music_ 

def caltime(musicinfo_): 
    starttime = musicinfo_[0]
    endtime = musicinfo_[1]
    hour = 1 * (int(endtime.split(':')[0]) - int(starttime.split(':')[0]))
    if hour == 0: 
        total = int(endtime.split(':')[1]) - int(starttime.split(':')[1])
    else: 
        total = 60 * hour + int(endtime.split(':')[1]) - int(starttime.split(':')[1])

    return total

def solution(m, musicinfos):
    answer = []
    m = changecode(m)
    for idx, musicinfo in enumerate(musicinfos): 
        musicinfo = changecode(musicinfo)
        musicinfo = musicinfo.split(',')
        time = caltime(musicinfo)

        # 길이가 시간보다 더 긴 경우 
        if len(musicinfo[3]) >= time :
            melody = musicinfo[3][0:time]
        else:             
            # 시간을 계산해서 몫과 나머지로 계산 
            # 다른 사람 풀이 : q, r = divmod(time,len(musicinfo[3]))
            a = time // len(musicinfo[3])
            b = time % len(musicinfo[3])
            melody = musicinfo[3] * a + musicinfo[3][0:b]
        # 노래가 melody에 포함되면 정답후보에 저장 
        if m in melody: 
            answer.append([idx, time, musicinfo[2]])
    # 정답이 있는 경우 
    if len(answer) != 0: 
        # time -> index 기준으로 정렬 
        answer = sorted(answer, key = lambda x: (-x[1], x[0]))
        return answer[0][2]
    # 정답이 없는 경우
    return "(None)"
"""
