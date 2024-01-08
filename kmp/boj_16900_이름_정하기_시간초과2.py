from sys import stdin
from collections import deque
import itertools

s, k = map(str,stdin.readline().split())
s_deque_tmp1 = deque(s)
s_deque_tmp2 = deque(s)

for i in range(len(s)):
    tmp1 = deque(itertools.islice(s_deque_tmp1, 1, len(s_deque_tmp2)))
    tmp2 = deque(itertools.islice(s_deque_tmp2, 0, len(s_deque_tmp2)-1))
    if tmp1 != tmp2:
        s_deque_tmp1.popleft()
        s_deque_tmp2.pop()
        continue
    else:
        tmp = s.replace(''.join(tmp2),"",1)
        s = deque(s) + deque(tmp) * (int(k)-1)
        break
print(len(''.join(s)))


