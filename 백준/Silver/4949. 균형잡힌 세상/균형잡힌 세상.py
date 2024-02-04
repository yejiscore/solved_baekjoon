import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    stack = []

    # 종료조건
    if string == '.':
        break

    for i in string:
        # 왼쪽 (스택 추가)
        if i == '(' or i == '[':
            stack.append(i)
        # 오른쪽 (스택 제거)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')