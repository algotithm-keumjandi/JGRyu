def solution(n, lost, reserve):
    tmp = n
    answer = 0
    for i, n in enumerate(reserve):
        # print(lost, reserve, "losttttt")
        if n in lost:
            reserve.pop(i)
            lost.remove(n)
            # print(lost, reserve, "----")
        elif n - 1 in lost:
            reserve.pop(i)
            lost.remove(n - 1)
            answer += 1
            # print(lost, reserve, "@@@")
        elif n + 1 in lost:
            reserve.pop(i)
            lost.remove(n + 1)
            answer += 1
        #     print(lost, reserve, "@@@")
        # print(tmp, len(lost), "?????")
    return tmp - len(lost)

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
