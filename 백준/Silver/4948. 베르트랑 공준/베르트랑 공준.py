import sys
import math

input = sys.stdin.readline

# 소수 판명
def is_primeNum(n):
    if n == 1:
        return False
    for i in range(2, math.trunc(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# 시간초과 방지 위해 주어진 범위의 숫자를 
primeNum_list = []
for i in range(2, 123456*2):
    if is_primeNum(i):
        primeNum_list.append(i)

n = int(input())

while True:
    cnt = 0
    if n == 0:
        break
    for i in primeNum_list:
        if n < i <= 2*n:
            cnt += 1
    print(cnt)
    n = int(input())