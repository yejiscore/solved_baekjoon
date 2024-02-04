import sys
input = sys.stdin.readline

for _ in range(int(input())):
    string = input().strip()
    while '()' in string:
        # str.replace(a,b) = 문자열 str 속 a를 b로 바꾼다.
        string = string.replace('()', '')
    print("NO" if string else "YES")