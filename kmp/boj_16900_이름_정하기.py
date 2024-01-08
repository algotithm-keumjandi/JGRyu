from sys import stdin
from collections import deque

inputs = stdin.readline
s, k = map(str,inputs().split())

def name(s, k):
    s_deque_tmp1, s_deque_tmp2 = deque(s), deque(s)
    for i in range(len(s)):
        s_deque_tmp1.popleft()
        s_deque_tmp2.pop()
        if s_deque_tmp1 != s_deque_tmp2:
            continue
        else:
            del s_deque_tmp1
            tmp = ''.join(s_deque_tmp2)
            del s_deque_tmp2
            keyword = s.replace(tmp,"",1)
            total_len = (int(k)-1) * len(keyword) + len(s)
            return total_len
total_len = name(s, k)
del name
print(total_len)
# print(''.join(s), len(''.join(s)))



# abbababbbbababababba 
# abbababbbbababababba
# babbbbababababba

# abc abcabcabca
# abcabcabca

# abcabcabca bca bca

# abcabca
# abcabca

