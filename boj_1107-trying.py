from sys import stdin
import math

ch_now = 100
ch_des = int(input().strip())
broken_num = int(input().strip())
broken_btn = []

if broken_num != 0:
    broken_btn = list(map(int, stdin.readline().strip().split(" ")))

if ch_des == 100:
    print(100)
    exit()

# 숫자 하나 씩 증감
def check_close_num(s):
    minus = [0, 0] # [증가 횟수, 최종 값]
    plus = [0, 0]
    n = int(s)
    while True:
        if n in broken_btn:
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
        if n in broken_btn:
            if n >= 9:
                plus[1] = n
                break
            n += 1
            plus[0] += 1
        else:
            plus[1] = n
            break
    # plus가 더 가깝고 remain_btn에 있을 때
    if minus[0] > plus[0] and plus[1] not in broken_btn:
        return plus[1]
    # 거리가 같을 때
    elif minus[0] == plus[0]:
        if plus[1] not in broken_btn:
            return plus[1]
        elif minus[1] not in broken_btn:
            return minus[1]
    # minus 더 가깝고 remain_btn에 있거나 plus가 remain에 없을 때
    elif minus[1] not in broken_btn:
        return minus[1]
    # minus가 remain에 없을 때
    elif plus[1] not in broken_btn:
        return plus[1]
    else:
        return int(s)
    return int(s)

# 숫자 전체 증감
def close_num_high(s):
    flag_p = True
    n_plus = int(s)
    while flag_p:
        flag_p = False
        n_plus += 1
        for d in str(n_plus):
            if int(d) in broken_btn:
                flag_p = True
                break
    return n_plus  

def close_num_low(s):    
    flag_m = True
    n_minus = int(s)
    while flag_m:
        flag_m = False
        if n_minus == 0:
            break
        n_minus -= 1
        for d in str(n_minus):
            if int(d) in broken_btn:
                flag_m = True
                break
    return n_minus

ch_og = ''
for s in str(ch_des):
    if int(s) not in broken_btn:
        ch_og += str(s)
    else:
        ch_og += str(check_close_num(s))


ch_tmp = ch_des
digit_count = 0
while (ch_tmp / 10) >= 1:
    ch_tmp = ch_tmp / 10
    digit_count += 1

ch_high, ch_low = 0, 0
ch_high2, ch_low2 = ch_tmp + 1, ch_tmp - 1

ch_high2 = math.floor(ch_high) * (10 ** digit_count)
ch_low2 = math.floor(ch_low) * (10 ** digit_count) + math.floor((10 ** digit_count) - 1)


if len(broken_btn) != 10:
    if broken_btn != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        # if ch_des >= 10:
        ch_high = close_num_high(ch_des)
        ch_low = close_num_low(ch_des)

ch_og = int(ch_og)
dis_og = abs(ch_og - ch_des)
dis_high = abs(ch_high - ch_des)
dis_low = abs(ch_low - ch_des)
dis_high2 = abs(ch_high2 - ch_des)
dis_low2 = abs(ch_low2 - ch_des)

dict_tmp = {dis_high: ch_high, dis_high2: ch_high2,  dis_og: ch_og, dis_low: ch_low, dis_low2: ch_low2}
dict_dic = dict_tmp.copy()

for i in dict_tmp.items():
    if i[1] in broken_btn:
        dict_dic.pop(i[0])

# dict안에 아무 것도 없으면
try:
    close_dis = min(dict_dic)
    ch_st = dict_dic[close_dis]
except:
    ch_st = 0

# 숫자 다 고장이면 채널 100에서 시작
if len(broken_btn) == 10:
    ch_st = 100
# 100 시작이 더 빠르면 채널 100에서 시작
if abs(ch_des - ch_st) > abs(ch_des - 100) or len(str(ch_st)) > abs(ch_des - 100):
    ch_st = 100

pushed = 0 # 총 버튼 누른 횟수

if ch_st == 100:
    pushed = abs(ch_des - ch_st)
elif ch_st == ch_des:
    pushed = len(str(ch_st))
else: 
    pushed = len(str(ch_st)) + abs(ch_des - ch_st)

print(pushed)
