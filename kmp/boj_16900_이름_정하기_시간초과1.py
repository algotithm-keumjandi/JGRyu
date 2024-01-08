import math
import time
from sys import stdin
s, k = map(str,stdin.readline().split())

tmp = ''
for i in range(int(k)-1):
    idx = len(s)-1
    while True:
        if len(tmp) == 0:
            tmp += s
        elif tmp[-idx:] == s[0:idx]:
            tmp += s[idx:]
            break
        else:
            idx -= 1
print(len(tmp))

