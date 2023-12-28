from sys import stdin
from collections import deque
bs = int(input()) # board_size
apple_loc = [list(map(int,stdin.readline().split())) for i in range(int(input()))]
rotate_snake = [list(stdin.readline().split()) for i in range(int(input()))]

# print(bs)
# print(apple_loc)
print(rotate_snake)

if rotate_snake[0][1] == 'L': # 처음 꺾는 방향이 왼쪽이면 바로 게임 종료
    print('왼쪽으로 꺾어서 바로 Game Over')
    print(f'Play Time: {rotate_snake[0][0]}')
    exit()

# nxn 행렬 생성
board = [[0 for col in range(bs)] for row in range(bs)]

# apple 추가, apple == 1
# row, col은 index -> 0 부터 시작: X
# 요구사항은 행, 열 -> 1 부터 시작: O
for row, col in apple_loc:
    board[row-1][col-1] = 1 # (row-1)행 (col-1)열: O

head_loc = [0, 0] # [row, col]

# 처음엔 무조건 [0, 0]에서 [0, 1]로 가야함
head_to_go = [head_loc[0], head_loc[1] + 1] # 머리가 다음에 갈 index
snake = deque([head_loc])
p_time = 0 # play_time
direction = 'D'

########################################################################
### 문제 풀 땐 필요 없는데 보기 편하게 만듦
########################################################################
def results(snake_loc, play_time, cause):
    print("Gane_Over")
    if cause == 1:
        print('몸통 충돌')
        for row, col in snake_loc: # 행렬에 뱀 위치=2 삽입해서 알아보기 편하게 출력
            board[row][col] = 2
    elif cause == 2:
        print('행 충돌')
        for row, col in snake_loc:
            board[row-1][col] = 2
    elif cause == 3:
        print('열 충돌')
        for row, col in snake_loc:
            board[row][col-1] = 2

    # 보기 편하게 행렬 출력
    for _ in board:
        print(_)
    # 뱀, play time 출력
    print(f'{snake} Play Time: {play_time}')


########################################################################
### 게임 시작
########################################################################
# rotate_snake 만큼 실행하다가 충돌하면 종료
for st, di in rotate_snake: # straight, direction
    ########################################################################
    ### TODO: 이 위치가 맞는지 확인 필요
    ########################################################################
    # for문 시작하기 전에 head가 갈 방향 정해주고
    head_di = [head_to_go[0] - head_loc[0], head_to_go[1] - head_loc[1]] # head_direction
    print(f'head_di: {head_di}')
    # sum(head_di) == -1: 머리 방향이 상/우
    #               == 1: 머리 방향이 하/좌
    # 상/우 -> D가 +, L이 - 임
    # 하/좌 -> D가 -, L이 + 임

    # 즉 sum(head_di) == 1 이면 
    #   D일 때 갈 방향: [0,-1]/[-1,0], L일 때 갈 방향: [0,1]/[1,0]
    # sum(head_di) == -1 이면
    #   D일 때 갈 방향: [0,1]/[1,0], L일 때 갈 방향: [0,-1]/[-1,0]

    if sum(head_di) == 1:
        # print("머리방향: 하/좌")
        di_to_go = 0 # D는 -, L은 +, direction_to_go
    else: # sum(head_di) == -1
        # print("머리방향: 상/우")
        di_to_go = 1 # D는 +, L은 -
    ########################################################################

    direction = di
    for i in range(int(st)):
        if head_loc != [0,0]:
            end_condition = (head_to_go in snake) or (head_to_go[0] > bs or head_to_go[0] < 0) or (head_to_go[1] > bs or head_to_go[1] < 0) # 게임 종료 조건
            print("update end_condition..")
        else:
            print("Game Start")
            end_condition = False

        if end_condition: # 자기 몸 or 벽 충돌 확인
            print(head_to_go, "head_to_go")
            # 게임 종료 원인 확인
            if head_to_go in snake:
                cause = 1
            elif head_to_go[0] > bs or head_to_go[0] < 0:
                cause = 2
            elif head_to_go[1] > bs or head_to_go[1] < 0:
                cause = 3
            results(snake, p_time, cause) # 여기까지는 풀 때 필요없음
            
            # 충돌하면 결과 출력하고 프로그램 실행 멈추기
            print(p_time)
            exit()
        else:
            snake.append(head_to_go) # 도착 지점 좌표 append
    
            if board[head_to_go[0]][head_to_go[1]] == 0: # 도착 지점의 좌표에 사과가 없으면
                snake.popleft() # 꼬리 pop
            p_time += 1
            print(f'{snake} {head_to_go} {head_loc} 뱀, head_to_go, head_loc')
            head_loc = head_to_go
            ########################################################################
            ### TODO: 다음 초에 앞으로 나아가게 head_to_go 초기화 필요
            ########################################################################
    ########################################################################
    ### TODO: move_to가 아니라 head_di가 맞는건지 확인 필요
    ########################################################################
    if di_to_go == 0: # 머리방향: 하/좌
        if direction == 'D': # minus
            move_to = [abs(head_di[1]) * -1, abs(head_di[0]) * -1] # head_di 뒤집기
            head_to_go = [head_loc[0] + move_to[0], head_loc[1] + move_to[1]]
        else: # plus
            move_to = [abs(head_di[1]), abs(head_di[0])]
            head_to_go = [head_loc[0] + move_to[0], head_loc[1] + move_to[1]]
    else: # 머리방향: 상/우
        if direction == 'D': # plus
            move_to = [abs(head_di[1]), abs(head_di[0])]
            head_to_go = [head_loc[0] + move_to[0], head_loc[1] + move_to[1]]
        else: # minus
            move_to = [abs(head_di[1]) * -1, abs(head_di[0]) * -1]
            head_to_go = [head_loc[0] + move_to[0], head_loc[1] + move_to[1]]
    print(head_loc, move_to, head_to_go, head_di, "head_loc, move_to, head_to_go, head_di")
    










