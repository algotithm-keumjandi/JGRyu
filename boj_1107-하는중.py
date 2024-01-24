from sys import stdin

updown_flag = 1

# 0에서 - 눌러도 0
# 채널 N으로 이동
# 고장난 버튼 알려줌
# N 으로 이동하기 위해 버튼 누르는 최소 횟수

ch_now = 100
ch_des = str(input().strip())
broken_num = int(input())
remain_btn = []
broken_btn = []

if broken_num != 0:
    broken_btn = list(map(str, stdin.readline().strip().split(" ")))
    remain_btn = [i for i in range(10) if str(i) not in broken_btn]
else:
    remain_btn = [i for i in range(10)]


# if ch_des <= 100:
#     tmp = 100 - ch_des
#     if tmp <= 2:
#         answer = tmp
#     else:
#         answer = 100 - ch_des

# ch_des의 모든 digit이 remain_btn에 있어야 가능
# if int(ch_des) == 100:
#     print(0) # ch_des가 100이면 끝
#     exit()
# elif int(ch_des) < 100:
#     print(2) # ch_des가 100보다 작으면
#     exit()
# elif int(ch_des) < 10 :
#     print(1) # ch_des가 10보다 작으면 버튼 1개로 가능 
#     exit()


print(remain_btn, "remain_btn")

def check_close_num(s):
    minus = [0, 0] # [증가 횟수, 최종 값]
    plus = [0, 0]
    n = int(s)
    while True:
        if n not in remain_btn:
            if n <= 0:
                minus[1] = n
                break
            n -= 1
            minus[0] += 1
        else:
            minus[1] = n
            break
    n = int(s)
    while True:
        if n not in remain_btn:
            if n >= 9:
                plus[1] = n
                break
            n += 1
            plus[0] += 1
        else:
            plus[1] = n
            break
    if minus[0] > plus[0] and plus[1] in remain_btn:
        return plus[1]
    elif minus[0] == plus[0]:
        if plus[1] in remain_btn:
            return plus[1]
        elif minus[1] in remain_btn:
            return minus[1]
    elif minus[1] in remain_btn:
        return minus[1]
    elif plus[1] in remain_btn:
        return plus[1]
    else:
        print("retrun " + s)
        return int(s)
    print("+- 오류2 @@@")
    return int(s)

short_way = -1 # +- 중 어떤 버튼을 눌러야 빠른지
ch_st = ''

for s in ch_des: # 최대 50만번
    if int(s) in remain_btn:
        ch_st += str(s)
    else:
        ch_st += str(check_close_num(s))

ch_des = int(ch_des)
ch_st = int(ch_st)

# 숫자 싹 다 고장이면 채널 100에서 시작
if len(broken_btn) == 10:
    ch_st = 100

# 100 시작이 더 빠르면 100으로 초기화
if abs(ch_des - ch_st) > abs(ch_des - 100):
    ch_st = 100

print(ch_des, ch_st, "목표 채널, 숫자 버튼으로 갈 채널")

# n = 0
# if ch_des > 100:
# 	n = ch_des - 100
# else: # ch_des < 100
# 	n = 100 - ch_des 






