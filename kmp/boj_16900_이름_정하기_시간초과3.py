from sys import stdin
from collections import deque

inputs = stdin.readline
s, k = map(str,inputs().split())
s_deque_tmp1, s_deque_tmp2 = deque(s), deque(s)

for i in range(len(s)):
    s_deque_tmp1.popleft()
    s_deque_tmp2.pop()
    if len(set({''.join(s_deque_tmp1), ''.join(s_deque_tmp2)})) == 2:
        continue
    else:
        s = s + s.replace(''.join(s_deque_tmp2),"",1) * (int(k)-1)
        break
print(len(''.join(s)))


# abbababbbbababababba 
# abbababbbbababababba
# babbbbababababba

# abc abcabcabca
# abcabcabca

# abcabcabca bca bca

# abcabca
# abcabca

