import math

n = int(input())
LCM = [[*map(int, input().split())] for _ in range(n)]

for i in range(len(LCM)):
    print(math.lcm(LCM[i][0], LCM[i][1]))