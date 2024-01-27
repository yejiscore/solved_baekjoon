import sys
import math

input = sys.stdin.readline

# 소수 판명하는 함수 정의
def is_primenum(n):
    for i in range(2, math.trunc(math.sqrt(n)+1)):
        if n % i == 0: # 소수가 아니면
            return False
    # for 문이 끝났는데도 나누었는데 나머지가 모두 0이 아니었다면 
    # 소수
    return True

m, n = map(int, input().split())

if m == 1:
    m += 1
for i in range(m, n+1):
    if is_primenum(i):
        print(i)