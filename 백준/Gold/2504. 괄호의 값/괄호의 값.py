import sys
arr = sys.stdin.readline().rstrip()

stack = []
ans = 0
var = 1
prev = ''

for i in arr:
    if i == '(':
        stack.append(i)
        var *= 2
        prev = i
    elif i == '[':
        stack.append(i)
        var *= 3
        prev = i
    elif i == ')':
        if not stack or stack[-1] != '(':
            ans = 0
            break
        if prev == '(':
            ans += var
        stack.pop()
        var //= 2
        prev = i
    elif i == ']':
        if not stack or stack[-1] != '[':
            ans = 0
            break
        if prev == '[':
            ans += var
        stack.pop()
        var //= 3
        prev = i
    else:
        ans = 0
        break

if stack:
    print(0)
else:
    print(ans)
