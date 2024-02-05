import sys
input = sys.stdin.readline

n = int(input())
student = list(map(int, input().split()))
stack = []

num = 1

while student:
    if student[0] == num:
        student.pop(0)
        num += 1
    else:
        stack.append(student.pop(0))

    while stack:
        if stack[-1] == num:
            stack.pop()
            num += 1
        else:
            break

print("Nice" if not stack else "Sad")