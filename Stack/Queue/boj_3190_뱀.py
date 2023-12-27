from sys import stdin
bs = int(input()) #board_size
apple_loc = [list(map(int,stdin.readline().split())) for i in range(int(input()))]
rotate_snake = [list(stdin.readline().split()) for i in range(int(input()))]

print(bs)
print(apple_loc)
print(rotate_snake)

l = []
for i in range(bs):
    l.append(i)


