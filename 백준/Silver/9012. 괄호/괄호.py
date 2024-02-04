import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    string = input().rstrip()
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append('(')
        else: # ')' 입력받았는데
            if not len(stack) == 0: # 앞서 '(' 를 입력했었다면
                stack.pop() # 삭제
            else: # 앞서 '('를 입력하지 않았다면
                stack.append(')') # 일단 ')' 입력 -> 마지막 if 문 조건 맞추기위해
                break
    if not len(stack) == 0:
        print("NO")
    else:
        print("YES")