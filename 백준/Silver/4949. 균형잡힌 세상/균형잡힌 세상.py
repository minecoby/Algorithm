import sys 
while True:
    stack = []
    content = sys.stdin.readline()
    if content == ".\n":
        break
    for i in content:
        if i == '[' or i == '(' :
            stack.append(i)
        if i == ")":
            if len(stack) == 0 or stack[-1] != "(":
                stack.append(i)
                break
            else:
                stack.pop()
        if i == "]":
            if len(stack) == 0 or stack[-1] != "[":
                stack.append(i)
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print("yes")
    else:
        print("no")