import sys

N = int(sys.stdin.readline())
ans = 0
for _ in range(N):
    stack = []
    arr = sys.stdin.readline().rstrip()
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i != stack[-1]:
                stack.append(i)
            else:
                stack.pop()
    if len(stack) == 0:
        ans += 1
print(ans)