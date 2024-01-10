from sys import stdin
from collections import deque

inputs = stdin.readline
s, k = map(str,inputs().split())

def name(s, k):
    s_deque_tmp1, s_deque_tmp2 = deque(s), deque(s)
    for i in range(len(s)):
        s_deque_tmp1.popleft(), s_deque_tmp2.pop()
        if s_deque_tmp1 == s_deque_tmp2:
            tmp = ''.join(s_deque_tmp2)
            keyword = s.replace(tmp,"",1)
            break
    return int(k)-1, len(keyword), len(s)
k, kw, len_s = name(s, k)
print(k * kw + len_s)

