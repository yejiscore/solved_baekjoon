import sys
import math

input = sys.stdin.readline

n = int(input().rstrip())
trees = [int(input().rstrip()) for _ in range(n)]

# 심어진 나무들의 간격을 구하기
interval = []
for i in range(0, n-1):
    interval.append(trees[i+1]-trees[i])

# 간격들의 최대공약수 구하기
gcd = interval[0]
for j in range(1, len(interval)):
    gcd = math.gcd(gcd, interval[j])

# 심을 나무 구하기
plant = 0
for tree in interval:
    plant += tree // gcd - 1

# 심어야할 나무 개수 출력하기
print(plant)