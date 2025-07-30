import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
que = deque((i+1, num) for i, num in enumerate(nums))
ans = []
while que:
    idx, move = que.popleft()
    ans.append(idx)
    if not que:
        break
    if move > 0:
        que.rotate(-(move-1))
    else:
        que.rotate(-move)  
print(*ans)
