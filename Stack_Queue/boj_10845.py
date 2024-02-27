from sys import stdin, stdout
from collections import deque
N = int(input())
l = ['push', 'pop', 'size', 'empty', 'front', 'back']
dq = deque()
for _ in range(N):
    s = stdin.readline().strip()
    if l[0] in s:
        s, n = s.split()
        dq.append(n)
    elif s == l[1]:
        stdout.write('-1'+ '\n' if len(dq) == 0 else dq.popleft() + '\n')
    elif s == l[2]:
        stdout.write(str(len(dq)) + '\n')
    elif s == l[3]:
        stdout.write('1'+ '\n' if len(dq) == 0 else '0'+ '\n')
    elif s == l[4]:
        stdout.write('-1'+ '\n' if len(dq) == 0 else dq[0] + '\n')
    elif s == l[5]:
        stdout.write('-1'+ '\n' if len(dq) == 0 else dq[-1] + '\n')

