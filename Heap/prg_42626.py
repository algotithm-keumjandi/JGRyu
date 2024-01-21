import heapq

def solution(scoville, K):
    repeat = 0
    heapq.heapify(scoville)

    # len(heap)이 2 이상, 최솟값이 K보다 이하면
    while len(scoville) >= 2 and scoville[0] < K:
        sm1 = heapq.heappop(scoville)
        sm2 = heapq.heappop(scoville)
        heapq.heappush(scoville, sm1 + sm2 * 2)
        repeat += 1

    # 다 합쳐도 K보다 작을 때
    if scoville[0] < K:
        return -1
    
    return repeat

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.1MB)
테스트 4 〉	통과 (0.01ms, 9.95MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.45ms, 10.2MB)
테스트 7 〉	통과 (0.51ms, 10.1MB)
테스트 8 〉	통과 (0.05ms, 10.1MB)
테스트 9 〉	통과 (0.04ms, 9.91MB)
테스트 10 〉	통과 (0.32ms, 10.1MB)
테스트 11 〉	통과 (0.20ms, 10.2MB)
테스트 12 〉	통과 (0.73ms, 10.1MB)
테스트 13 〉	통과 (0.68ms, 10MB)
테스트 14 〉	통과 (0.02ms, 10.2MB)
테스트 15 〉	통과 (0.98ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.1MB)
테스트 18 〉	통과 (0.00ms, 10.2MB)
테스트 19 〉	통과 (0.01ms, 10.1MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
테스트 21 〉	통과 (0.00ms, 10.3MB)
테스트 22 〉	통과 (0.00ms, 10.1MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
테스트 24 〉	통과 (0.01ms, 10.2MB)
테스트 25 〉	통과 (0.01ms, 10.3MB)
테스트 26 〉	통과 (0.02ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (169.74ms, 16.1MB)
테스트 2 〉	통과 (363.39ms, 21.6MB)
테스트 3 〉	통과 (1830.23ms, 49.7MB)
테스트 4 〉	통과 (148.26ms, 14.9MB)
테스트 5 〉	통과 (1703.55ms, 51.7MB)
'''