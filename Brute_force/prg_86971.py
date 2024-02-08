from collections import deque
def solution(n, wires):

    def count_node(n, wires):
        graph = [[False] * (n+1) for _ in range(n+1)]

        for a, b in wires:
            graph[a][b] = True
            graph[b][a] = True

        visit = [False] * (n+1)
        node_num = 0
        queue = deque()
        queue.appendleft(n)
        while queue:
            next_node = queue.pop()
            if visit[next_node]: continue
            visit[next_node] = True
            node_num += 1
            for i in range(1, len(visit)):
                if not graph[next_node][i] : continue
                queue.appendleft(i)
        return node_num

    node_diff = []
    for i in range(len(wires)):
        wires_tmp = wires.copy()
        disconnect = wires_tmp.pop(i)
        node_num1 = count_node(n, wires_tmp)
        node_num2 = n - node_num1
        # print(f"연결 노드 수: {node_num1}, disconnect: {disconnect}")
        node_diff.append(abs(node_num1 - node_num2))
    return min(node_diff)

'''
[전력망을 둘로 나누기]

정확성  테스트
테스트 1 〉	통과 (54.37ms, 10.3MB)
테스트 2 〉	통과 (34.38ms, 10.3MB)
테스트 3 〉	통과 (29.94ms, 10.4MB)
테스트 4 〉	통과 (37.77ms, 10.3MB)
테스트 5 〉	통과 (46.87ms, 10.4MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.4MB)
테스트 8 〉	통과 (0.53ms, 10.2MB)
테스트 9 〉	통과 (0.43ms, 10.2MB)
테스트 10 〉	통과 (36.98ms, 10.2MB)
테스트 11 〉	통과 (49.42ms, 10.3MB)
테스트 12 〉	통과 (40.97ms, 10.3MB)
테스트 13 〉	통과 (36.76ms, 10.4MB)
'''