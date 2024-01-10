from sys import stdin

inputs = stdin.readline
# s, k = map(str,inputs().split())
s = "aaaaba"
k = 2
# s = "abcabcabca"
# k = 3
# s = "abbababbbbababababba"
# k = 2
s = "aaaabaab"
k = 2


table = [0 for _ in range(len(s))]
i = 0
for j in range(1, len(s)):
    while i > 0 and s[i] != s[j]:
        i = table[i-1]
    if s[i] == s[j]:
        i += 1
        table[j] = i
print(table, "table")
print(len(s) + (len(s) - max(table)) * (int(k) - 1), "tot len")

# 아닌 듯
m = max(table)
max_values = [index + 1 for index, val in enumerate(table) if val == m]
max_idx = max(max_values)

pattern_len = len(s) - max(table)
print(max_idx, pattern_len, "max_idx, ptrn_len")
print(s[-pattern_len : max_idx+1])

if table[-1] == 0:
    pattern_len



# 반례: aaaaab 2

# def kmp(s, pattern):
#     table2 = [0 for _ in range(len(pattern))]
#     i = 0
#     for j in range(1, len(pattern)):
#         while i > 0 and pattern[i] != pattern[j]:
#             i = table2[i-1]
#         if pattern[i] == pattern[j]:
#             i += 1
#             table2[j] = i

#     result = []
#     i = 0
#     for j in range(1, len(s)):
#         while i > 0 and pattern[i] != s[j]:
#             i = table2[i-1]
#         if pattern[i] == s[j]:
#             i += 1
#             if i == len(pattern):
#                 result.append(j - i + 1)
#                 i = table2[i-1]
#     return result

# print(kmp("abcabcabca", "bca"))
# print(kmp("abbababbbbababababba", "babbbbababababba"))
# print(kmp("aaaaaaab", "aaaaaaab"))
