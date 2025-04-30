import sys

N = int(sys.stdin.readline())
arr = []
stack = []

ans = 0

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

for i in arr:
    while len(stack) and stack[-1] <= i:
        stack.pop()
    stack.append(i)
    ans += len(stack)-1
    
print(ans)