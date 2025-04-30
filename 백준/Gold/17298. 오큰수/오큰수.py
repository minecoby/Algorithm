N = int(input())
arr = list(map(int,input().split()))

ans = [-1] * N
stack = []
for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        ans[stack.pop()] = arr[i]
    stack.append(i)
for i in ans:
    print(i, end=" ")