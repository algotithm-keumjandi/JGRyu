from sys import stdin
import math
updown_flag = 1

# 0에서 - 눌러도 0
# 채널 N으로 이동
# 고장난 버튼 알려줌
# N 으로 이동하기 위해 버튼 누르는 최소 횟수

ch_now = 100
ch_des = int(input().strip())
broken_num = int(input().strip())
remain_btn = []
broken_btn = []
pushed = 0 # 총 버튼 누른 횟수

if broken_num != 0:
    broken_btn = list(map(str, stdin.readline().strip().split(" ")))
    remain_btn = [i for i in range(10) if str(i) not in broken_btn]
else:
    remain_btn = [i for i in range(10)]


ch_tmp = ch_des
digit_count = 0
while (ch_tmp / 10) >= 1:
    ch_tmp = ch_tmp / 10
    digit_count += 1

# 한자리수면 그냥 +1 -1
ch_high = ch_tmp + 1
ch_low = ch_tmp - 1

# ch_des의 앞자리 +1 하고 나머지 자리는 0으로 변경
ch_high = math.floor(ch_high) * (10 ** digit_count)
# ch_des의 앞자리 -1 하고 나머지 자리는 9으로 변경
ch_low = math.floor(ch_low) * (10 ** digit_count) + math.floor((10 ** digit_count) - 1)
print("ch_high:", ch_high, "| ch_low:", ch_low, "| digit_count:", digit_count,)

digit_count = 0



# round(1)



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


# ch_high, ch_low, ch_des에서 고장난 버튼 빼고 가장 가까운 값으로 변경
ch_high2 = ''
for s in str(ch_high): # 최대 50만번
    if int(s) in remain_btn:
        ch_high2 += str(s)
    else:
        ch_high2 += str(check_close_num(s))

ch_low2 = ''
for s in str(ch_low):
    if int(s) in remain_btn:
        ch_low2 += str(s)
    else:
        ch_low2 += str(check_close_num(s))

ch_des2 = ''
for s in str(ch_des):
    if int(s) in remain_btn:
        ch_des2 += str(s)
    else:
        ch_des2 += str(check_close_num(s))

print("ch_high2:", ch_high2, "| ch_low2:", ch_low2, "| ch_des2:", ch_des2)

ch_st_high = int(ch_high2)
ch_st_low = int(ch_low2)
ch_st_og = int(ch_des2)

short_way = -1 # +- 중 어떤 버튼을 눌러야 빠른지
dis_high = abs(ch_st_high - ch_des)
dis_low = abs(ch_st_low - ch_des)
dis_og = abs(ch_st_og - ch_des)

# key 겹치면(거리가 같으면) 작은걸 우선으로 넣어야 해서
# 넣을 때 순서 지켜야함 (high > og > low)
dict_dic = {dis_high: ch_st_high, dis_og: ch_st_og, dis_low: ch_st_low}
close_dis = min(dis_high, dis_low, dis_og)

print(dict_dic)
for i in dict_dic:
    print(i, "@@@")

# tmp = min(dict_dic, key=lambda x : len(str(x)))
# print(tmp, "tmp")
print("가장 가까운 거리:", close_dis)


# 거리가 같으면 작은 값을 우선 해야 함.
# for i in str()
# if 

ch_st = dict_dic[min(dis_high, dis_low, dis_og)]

# 숫자 싹 다 고장이면 채널 100에서 시작
if len(broken_btn) == 10:
    ch_st = 100
# 100 시작이 더 빠르면 100으로 초기화
if abs(ch_des - ch_st) > abs(ch_des - 100):
    pushed = 0
    ch_st = 100

print(ch_des, ch_st, "목표 채널, 숫자 버튼으로 갈 채널")







