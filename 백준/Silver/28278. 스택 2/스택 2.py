import sys


n = int(sys.stdin.readline())
stack = []

for i in range(n):
    select = sys.stdin.readline().split()
    if select[0] == "1":
        stack.append(select[1])
    if select[0] == "2":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    if select[0] == "3":
        print(len(stack))
    if select[0] == "4":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    if select[0] == "5":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])
