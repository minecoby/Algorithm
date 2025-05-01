import sys
arr = sys.stdin.readline()
stack = []
ans = 0
lazer = True
for i in arr:
    if i == ")":
        if stack[-1] == "(" and lazer == False:
            stack.pop()
            ans += len(stack)
            lazer = True
        elif stack[-1] == "(":
            stack.pop()
            ans += 1
    if i == "(":
        stack.append("(")
        lazer = False
print(ans)