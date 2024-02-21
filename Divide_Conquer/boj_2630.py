from sys import stdin, stdout
from collections import deque, UserList

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, stdin.readline().split())))

tot_0 = tot_1 = 0

def divide(matrix, seg_len, tot_0, tot_1):
    count_0 = count_1 = 0
    for l in matrix:
        count_0 += l.count(0)
        count_1 += l.count(1)

    if count_0 == 0 or count_1 == 0:
        if matrix[0][0] == 0:
            tot_0 += 1
            return tot_0, tot_1
        elif matrix[0][0] == 1:
            tot_1 += 1
            return tot_0, tot_1
    matrix_tmp = []
    seg_len_tmp = seg_len // 2
    
    for l in matrix[:seg_len_tmp]:
        matrix_tmp.append(l[:seg_len_tmp])
    tot_0, tot_1 = divide(matrix_tmp, seg_len_tmp, tot_0, tot_1)
    matrix_tmp = []

    for l in matrix[:seg_len_tmp]:
        matrix_tmp.append(l[seg_len_tmp:])
    tot_0, tot_1 = divide(matrix_tmp, seg_len_tmp, tot_0, tot_1)
    matrix_tmp = [] 

    for l in matrix[seg_len_tmp:]:
        matrix_tmp.append(l[:seg_len_tmp])
    tot_0, tot_1 = divide(matrix_tmp, seg_len_tmp, tot_0, tot_1)
    matrix_tmp = []

    for l in matrix[seg_len_tmp:]:
        matrix_tmp.append(l[seg_len_tmp:])
    tot_0, tot_1 = divide(matrix_tmp, seg_len_tmp, tot_0, tot_1)

    return tot_0, tot_1

tot_0, tot_1 = divide(matrix, len(matrix), tot_0, tot_1)
print(tot_0)
print(tot_1)
