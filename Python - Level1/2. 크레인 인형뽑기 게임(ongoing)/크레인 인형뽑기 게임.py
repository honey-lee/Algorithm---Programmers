board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

#2차원 배열 리스트에 접근하는 함수 선언
def solution(board, moves):
    #뽑은 인형들을 담아줄 빈 리스트
    new_list= []
    #터지는 인형의 갯수를 세줄 변수
    cnt = 0

    #인형들을 뽑을 때마다 새로운 리스트에 넣어주고 뽑힌 인형은 기존 리스트에서 제거
    #여기서 궁금한점... 2차원 배열 리스트 뒤집는 방법
    for i in moves:
        new_list.append(board[i-1][-1])
        board[i-1].pop()

    #새 리스트에서 0을 모두 제거해준다
    for i in new_list:
        if i == 0:
            new_list.remove(0)

    #0이 제거되어서 뽑혀있는 인형들만 리스트에 남아있는 상태
    #같은 인형이 뽑혀있을 경우 터지는 인형에 2를 더해준다
    #여기서 값이 잘 나오지 않는 상황 (3 3 3 과 같이 같은 인형이 연속으로 3번 뽑혔을 경우 2개만 터져서 엣지케이스 발생)
    #for idx in range(1, len(new_list)-1):
        #if new_list[idx] == new_list[idx-1]:
            #cnt += 2

    for idx in range(1, len(new_list)-1):
        if new_list[idx] == new_list[idx+1]:
            cnt += 2

    return cnt

print(solution(board, moves))