from sys import stdin
from collections import deque
bs = int(input()) # board_size
apple_loc = [list(map(int,stdin.readline().split())) for i in range(int(input()))]
rotate_snake = [list(stdin.readline().split()) for i in range(int(input()))]

# e.g, 8 10 11 13 -> 8 2 1 2
tmp = [i for i in dict(rotate_snake).keys()]
for i, n in enumerate(tmp[1::]):
    rotate_snake[i+1][0] = str(int(n) - int(tmp[i]))

# print(bs)
# print(apple_loc)
# print(rotate_snake)

if rotate_snake[0][1] == 'L': # 처음 꺾는 방향이 왼쪽이면 바로 게임 종료
    print('왼쪽으로 꺾어서 바로 Game Over')
    print(f'Play Time: {rotate_snake[0][0]}')
    exit()


def make_board(bs, apple_loc):
    # nxn 행렬 생성
    board = [[0 for col in range(bs)] for row in range(bs)]

    # apple 추가, apple == 1
    # row, col은 index -> 0 부터 시작: X
    # 요구사항은 행, 열 -> 1 부터 시작: O
    for row, col in apple_loc:
        board[row-1][col-1] = 1 # (row-1)행 (col-1)열: O
    return board

board = make_board(bs, apple_loc)

head_loc = [0, 0] # [row, col]

# 처음엔 무조건 [0, 0]에서 [0, 1]로 가야함
head_to_go = [head_loc[0], head_loc[1] + 1] # 머리가 다음에 갈 index
snake = deque([head_loc])
p_time = 1 # play_time
trial = 0 # reccurent num
direction = 'D'

########################################################################
### 문제 풀 땐 필요 없는데 보기 편하게 만듦
########################################################################
def results(snake_loc, play_time, cause):
    if cause == 1:
        # print('몸통 충돌')
        board = make_board(bs, apple_loc)
        for row, col in snake_loc: # 행렬에 뱀 위치=2 삽입해서 알아보기 편하게 출력\
            board[row][col] = 2
    elif cause == 2:
        # print('행 충돌')
        board = make_board(bs, apple_loc)
        for row, col in snake_loc:
            board[row-1][col] = 2
    elif cause == 3:
        # print('열 충돌')
        board = make_board(bs, apple_loc)
        for row, col in snake_loc:
            board[row][col-1] = 2

    # 보기 편하게 행렬 출력
    for _ in board:
        print(_)
    # 뱀, play time 출력
    print(f'Play Time: {play_time} SNAKE: {list(snake)}')


########################################################################
### 게임 함수
########################################################################
def game_start(rotate_snake, head_loc, head_to_go, p_time, trial):
    # rotate_snake 만큼 실행하다가 충돌하면 종료
    for st, di in rotate_snake: # straight, direction
        direction = di
        head_di = [head_to_go[0] - head_loc[0], head_to_go[1] - head_loc[1]] # head_direction
        # print(f'head_di: {head_di}')
        # head_di[0] != 0: 머리 방향이 상/하
        #            == 0: 머리 방향이 좌/우
        if head_di[0] == 0:
            # print("머리방향: 좌/우")
            di_to_go = 0
        else: # head_di[0] != 0
            # print("머리방향: 상/하")
            di_to_go = 1

        for i in range(int(st)):
            if head_loc != [0,0] or trial != 0:
                end_condition = (head_to_go in snake) or (head_to_go[0] >= bs or head_to_go[0] < 0) or (head_to_go[1] >= bs or head_to_go[1] < 0) # 게임 종료 조건
                # print("update end_condition..")
            else:
                # print("Game Start")
                end_condition = False

            if end_condition: # 자기 몸 or 벽 충돌 확인
                # print(f'Cannot go to {head_to_go}')
                # 게임 종료 원인 확인
                if head_to_go in snake:
                    cause = 1
                elif head_to_go[0] >= bs or head_to_go[0] < 0:
                    cause = 2
                elif head_to_go[1] >= bs or head_to_go[1] < 0:
                    cause = 3
                # results(snake, p_time, cause) # results 함수는 제출할 때 필요없음
                
                # 충돌하면 결과 출력하고 프로그램 실행 멈추기
                print(p_time)
                exit()
            else:
                p_time += 1
                snake.append(head_to_go) # 도착 지점 좌표 append

                if board[head_to_go[0]][head_to_go[1]] == 0: # 도착 지점의 좌표에 사과가 없으면
                    snake.popleft() # 꼬리 pop
                    # print(f'POP Tail..')
                else:
                    board[head_to_go[0]][head_to_go[1]] = 0
                # print(f'{snake} {head_to_go} {head_loc} {head_di} 뱀, head_to_go, head_loc, head_di')

                head_loc = head_to_go
                head_to_go = [head_to_go[0] + head_di[0], head_to_go[1] + head_di[1]]
                ########################################################################
                # process 확인
                ########################################################################
                # results(snake, p_time, 1)

        # print(f'di_to_go: {di_to_go}, direction: {direction}')
        if di_to_go == 0: # 머리방향: 좌/우
            if head_di[1] == 1: # 머리방향: 우
                check_DL = 1 if direction == 'D' else -1 # D==1 L==-1
                head_di = [abs(head_di[1]) * check_DL, abs(head_di[0])] # head_di 뒤집기
                head_to_go = [head_loc[0] + check_DL, head_loc[1]]
            else: # 머리방향: 좌
                check_DL = -1 if direction == 'D' else 1 # D==-1 L==1
                head_di = [abs(head_di[1]) * check_DL, abs(head_di[0])]
                head_to_go = [head_loc[0] + check_DL, head_loc[1]]
        else: # 머리방향: 상/하
            if head_di[0] == 1: # 머리방향: 하
                check_DL = -1 if direction == 'D' else 1 # D==-1 L==1
                head_di = [abs(head_di[1]), abs(head_di[0]) * check_DL]
                head_to_go = [head_loc[0], head_loc[1] + check_DL]
            else: # 머리방향: 상
                check_DL = 1 if direction == 'D' else -1 # D==1 L==-1
                head_di = [abs(head_di[1]), abs(head_di[0]) * check_DL]
                head_to_go = [head_loc[0], head_loc[1] + check_DL]
        # print(head_loc, head_to_go, head_di, "head_loc, head_to_go, head_di")
    trial += 1
    if end_condition == False:
        game_start(rotate_snake, head_loc, head_to_go, p_time, trial)
        

########################################################################
### 게임 시작
########################################################################
game_start(rotate_snake, head_loc, head_to_go, p_time, trial)







