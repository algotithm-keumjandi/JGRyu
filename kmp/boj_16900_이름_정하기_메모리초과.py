from sys import stdin
from collections import deque

s, k = map(str,stdin.readline().split())
s_deque_tmp1, s_deque_tmp2 = deque(s), deque(s)


for i in range(len(s)):
    s_deque_tmp1.popleft()
    s_deque_tmp2.pop()
    if s_deque_tmp1 != s_deque_tmp2:
        continue
    else:
        tmp = s.replace(''.join(s_deque_tmp2),"",1)
        s = deque(s) + deque(tmp) * (int(k)-1)
        break
print(len(''.join(s)))
