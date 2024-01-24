# 문자열 정렬 문제
from sys import stdin
answer = [stdin.readline().strip() for i in range(int(input()))]

# abc 순으로 정렬
answer = sorted(list(set(answer)))
# 길이 순으로 정렬
answer = sorted(answer, key=lambda x: len(x))
for i in answer:
    print(i)
