from sys import stdin
from collections import deque

inputs = stdin.readline
s, k = map(str,inputs().split())
s_deque1, s_deque2 = deque(s), deque(s)

for _ in range(len(s)):
    s_deque1.popleft()
    s_deque2.pop()
    if s_deque1 == s_deque2:
        break

len_k = len(s) - len(s_deque2)
print((int(k)-1) * len_k + len(s))

