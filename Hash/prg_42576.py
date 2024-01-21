def solution(participant, completion):
    hash_sum = 0
    part = {}
    for i in participant:
        hash_sum += hash(i)
        part[hash(i)] = i
    for i in completion:
        hash_sum -= hash(i)
    return part[hash_sum]

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.1MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.36ms, 10.3MB)
테스트 4 〉	통과 (0.40ms, 10.4MB)
테스트 5 〉	통과 (0.41ms, 10.5MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (23.09ms, 23.9MB)
테스트 2 〉	통과 (30.39ms, 28.3MB)
테스트 3 〉	통과 (42.13ms, 31.1MB)
테스트 4 〉	통과 (43.25ms, 37.6MB)
테스트 5 〉	통과 (43.59ms, 37.7MB)
'''
