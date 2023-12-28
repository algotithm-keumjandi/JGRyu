l =[-1,1, 0]
print(l[:-1])


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




아래, D
head_loc + 0 -1
아래, L
head_loc + 0 1


왼, D
head_loc +  -1 0
왼, L
head_loc +  1 0


위, D
head_loc + 0 1
위, L
head_loc + 0 -1


오른, D
head_loc +  1 0
오른, L
head_loc +  -1 0
'''
