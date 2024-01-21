from sys import stdin
from collections import deque
import itertools
import re

inputs = stdin.readline
s, k = map(str,inputs().split())
s_deque1, s_deque2 = deque(s), deque(s)

for _ in range(len(s)):
    s_deque1.popleft()
    s_deque2.pop()
    
    tf = set(map(lambda x: x[0]==x[1], zip(s_deque1, s_deque2)))
    if len(tf) == 1 and list(tf)[0] == True:
        break
    # if s_deque1 == s_deque2:
    #     break

len_k = len(s) - len(s_deque2)
print((int(k)-1) * len_k + len(s))



# table = [0 for _ in range(len(s))]
# i = 0
# for j in range(1, len(s)):
#     while i > 0 and s[i] != s[j]:
#         i = table[i-1]
#     if s[i] == s[j]:
#         i += 1
#         table[j] = i

# print(len(s) + (len(s) - max(table)) * (int(k) - 1))





