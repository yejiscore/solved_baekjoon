import sys
input = sys.stdin.readline

primeNum = []
check = [0]*1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        primeNum.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

t = int(input())
for _ in range(t):
    cnt = 0
    n = int(input())
    for i in primeNum:
        if i >= n:
            break
        if check[n-i] == 0 and i <= n-i:
            cnt += 1
    print(cnt)