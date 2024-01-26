import math

a, b = map(int, input().split())
c, d = map(int, input().split())

rf_m = a*d+b*c
rf_d = b*d

gcd = math.gcd(rf_m, rf_d)

print(rf_m//gcd, rf_d//gcd)