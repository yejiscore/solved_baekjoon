import sys
import math

input = sys.stdin.readline

# 소수 판명하는 함수 정의
def is_primenum(n):
    for i in range(2, math.trunc(math.sqrt(n)+1)):
        if n % i == 0: # 소수가 아니면
            return False
    # for 문이 끝났는데도 나누었는데 나머지가 모두 0이 아니었다면 
    # = 소수
    return True

# 테스트 케이스의 개수 입력
n = int(input().rstrip())

# n줄에 하나씩 입력되는 테스트 케이스를 리스트로 저장
prime_num = [int(input().rstrip()) for _ in range(n)]

for i in range(n):
    while True: # 소수 판명이 나온다면 끝내는 while 문
        # 입력된 수가 0 혹은 1 이면 이 두 수보다 큰 수 중 작은 소수는 2뿐이다.
        if prime_num[i] == 0 or prime_num[i] == 1:
            print(2)
            break
        # 2 이상인 수가 입력된다면
        if is_primenum(prime_num[i]): # True 반환 -> 즉, 소수라면
            print(prime_num[i])
            break
        else: # False 반환 -> 소수가 아니라면
            prime_num[i] += 1 # 그 다음 수를 살펴보기