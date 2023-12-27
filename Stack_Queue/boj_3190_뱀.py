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
p_to_go = [head_loc[0], head_loc[1] + 1] # place_to_go
snake = deque([head_loc])
flag_game = True
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
        for row, col in snake_loc: # 행렬에 뱀 위치=2 삽입해서 알아보기 편하게 출력
            board[row-1][col] = 2
    elif cause == 3:
        print('열 충돌')
        for row, col in snake_loc: # 행렬에 뱀 위치=2 삽입해서 알아보기 편하게 출력
            board[row][col-1] = 2

    # 보기 편하게 행렬 출력
    for _ in board:
        print(_)
    # 뱀, play time 출력
    print(f'{snake} Play Time: {play_time}')


########################################################################
### flag_game = false일 때 까지 게임 진행
########################################################################
while flag_game:
    # for문 시작하기 전에 head가 갈 방향(상하좌우) 정해주고
    di_to_go = [p_to_go[0] - head_loc[0], p_to_go[1] - head_loc[1]] # direction_to_go

    # sum(di_to_go) == -1: 머리 방향이 상/우
    #               == 1: 머리 방향이 하/좌
    # 상/우 -> D가 +, L이 - 임
    # 하/좌 -> D가 -, L이 + 임

    # 즉 sum(di_to_go) == 1 이면 
    #   D일 때 갈 방향: [0,-1]/[-1,0], L일 때 갈 방향: [0,1]/[1,0]
    # sum(di_to_go) == -1 이면
    #   D일 때 갈 방향: [0,1]/[1,0], L일 때 갈 방향: [0,-1]/[-1,0]

    ########################################################################
    ### TODO: head가 갈 방향(상하좌우) 정하고, 그에 따라 di_to_go 조정
    ### 근데 여기서 하는게 맞을진 아직 모름
    ########################################################################
    print(f'direction_to_go {di_to_go}')
    if sum(di_to_go) == 1:
        print("머리방향: 하/좌")
    else:
        print("머리방향: 상/우")

    # rotate_snake 만큼 실행하다가 충돌하면 종료
    for st, di in rotate_snake: # straight, direction
        direction = di # 좌우(D/L) 방향 초기화
    
        
        if (p_to_go in snake) or (p_to_go[0] > bs) or (p_to_go[1] > bs): # 자기 몸 or 벽 충돌 확인
            # 게임 종료 원인 확인
            if p_to_go in snake:
                cause = 1
            elif p_to_go[0] > bs:
                cause = 2
            elif p_to_go[1] > bs:
                cause = 3
            results(snake, p_time, cause) # 여기까지는 풀 때 필요없음
            
            # 충돌하면 while문, for문 나가기
            flag_game = False
            break
        else:
            ########################################################################
            ### TODO: p_to_go 좌표 계산 필요
            ########################################################################
            snake.append(p_to_go) # 도착 지점 좌표 append
            print(f'{snake} {p_to_go} 뱀, 도착 지점 좌표')
            if board[p_to_go[0]][p_to_go[1]] == 0: # 도착 지점의 좌표에 사과가 없으면
                snake.popleft() # 꼬리 pop
            p_time += 1

            head_loc = p_to_go

        ########################################################################
        ### TODO: p_to_go 계산 여기서 하는게 맞나 체크하고 맞으면 코드수정
        ########################################################################
        if direction == 'D':
            p_to_go = [head_loc[0] + di_to_go[0], head_loc[1] + di_to_go[1]] # 방향에 따라 고쳐야함
        else:
            p_to_go = [head_loc[0] + di_to_go[0], head_loc[1] + di_to_go[1]] # 방향에 따라 고쳐야함








