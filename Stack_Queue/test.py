from sys import stdin
l =[-1,1, 0]
print(l[:-1])

# rotate_snake = [list(map(lambda x: x, stdin.readline().split())) for i in range(int(input()))]
# print(rotate_snake)

b = 1
a = 1 if b == 0 else 2
print(a)

'''
하좌상우 head_di
1 0
0 -1
-1 0
0 1

하좌상우 head_di 뒤집기:
0 1
	D: 0 -1
	L: 0 1
-1 0
	D: -1 0
	L: 1 0
0 -1
	D: 0 1
	L: 0 -1
1 0
	D: 1 0
	L: -1 0

head_loc = 0 3 일 때

head_di = -1 0
상 -> D
0 3 + 0 1
상 -> L
0 3 + 0 -1


head_di = 1 0
하 -> D
0 3 + 0 -1
하 -> L
0 3 + 0 1


head_di = 0 -1
좌 -> D
0 3 + -1 0
좌 -> L
0 3 + 1 0


head_di = 0 1
우 -> D
0 3 + 1 0
우 -> L
0 3 + -1 0
'''
