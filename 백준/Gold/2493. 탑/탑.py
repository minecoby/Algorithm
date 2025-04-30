import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
stack = []
result = []

for i in range(N):
    while stack and stack[-1][1] < towers[i]:
        stack.pop()
    
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0] + 1)  
    
    stack.append((i, towers[i]))

print(' '.join(map(str, result)))
