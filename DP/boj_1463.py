N = int(input())

def function(x):
    if x <= 3:
        return 1 if x != 1 else 0
    return min(function(x // 3) + x % 3 + 1, function(x // 2) + x % 2 + 1)
print(function(N))

##################################################################
# function(x // 3) + x % 3 + 1 에서
# 1. "+ 1": 역할
# 2. 나누어 떨어지지 않아도 "//"을 사용하면 내림과 같은 
#    역할을 하기 때문에, -1을 하는 것과 같다.
##################################################################
# e.g, function(10)
# -> min(function(3) + 2, function(5) + 1)
# -> min(1 + 2, function(2) + 2)
# -> min(1 + 2, 1 + 2)
# -> 3
##################################################################

### Test Cases ###
# print(function(1))
# print(function(2))
# print(function(3))
# print(function(4))
# print(function(10))
# print(function(16))
# print(function(25))
# print(function(80))
# print(function(10000))
# print(function(99681))
# print(function(99777))
# print(function(1000000))
