board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

# [[0, 0, 0, 4, 3],
# [0, 0, 2, 2, 5],
# [0, 1, 5, 4, 1],
# [0, 0, 0, 4, 3],
# [0, 3, 1, 2, 1]]

def solution(board, moves):
    # 인형을 쌓아둘 stack
    stack = []
    # 터진 인형의 수를 셀 stack
    result = 0
    # 게임판을 재배열할 리스트
    doll_board = []

    # 리스트의 행과 열을 뒤집어주기
    for i in zip(*board):
        doll_board.append(list(i))

    # 위의 공백을 모두 없애주자
    for i in range(len(doll_board)):
        while doll_board[i][0] == 0:
            doll_board[i].pop(0)

    for move in moves:
        # 해당 행이 비어있는 상태라면 아무 동작하지 않고 끝냄
        if len(doll_board[move-1]) == 0:
            continue
        # 해당 행이 비어있지 않고
        # 0번 인덱스에 값이 있을 경우
        # stack에 넣고 stack에 들어간 값은 삭제
        else:
            if doll_board[move-1][0]:
                stack.append(doll_board[move-1][0])
                doll_board[move-1].pop(0)

    # while True를 두고
    # 인형이 2개 같은 동안 계속 반복
    while True:
        # count 변수를 0으로 두고
        count = 0
        # 2개 간격으로 stack을 순회하면서
        for idx in range(0, len(stack) - 1):
            # 앞뒤가 같으면 idx를 2번 pop
            if stack[idx] == stack[idx + 1]:
                # 이 때 주의할점은 pop이후에 각 idx가 바뀌니까
                # idx만 2번 pop
                stack.pop(idx)
                stack.pop(idx)
                # result 변수 2 올리고
                # count 변수도 올린다
                result += 2
                count += 2
                break

        # 리스트 전체 순회하고도 연속으로 같은게 없어서
        # 멈추지 않았으면 while문 탈출
        # 아니면 위의 리스트 검사 반복
        if count == 0:
            break

    return result

print(solution(board, moves))


