import sys
import math

input = sys.stdin.readline

# 에라토스테네스의 체 알고리즘
array = [True for i in range(1000001)]

for i in range(2, int(math.sqrt(1000000))+1):
    if array[i] == True:
        j = 2
        while i*j <= 1000000:
            array[i*j] = False
            j += 1

t = int(input())
lst = [int(input()) for _ in range(t)]
for i in range(t):
    cnt = 0
    num = lst[i]
    for j in range(2, (num//2)+1):
        if array[j] and array[num-j]:
            cnt += 1
    print(cnt)