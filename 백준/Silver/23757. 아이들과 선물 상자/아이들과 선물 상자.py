import heapq
import sys

N,M = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
heap = []
for i in arr:
    heapq.heappush(heap,(-i,i))
arr = list(map(int,sys.stdin.readline().split()))
ans = 1
for i in arr:
    p = heapq.heappop(heap)
    if p[1] >= i:
        heapq.heappush(heap,(-(p[1]-i), p[1]-i))
    else:
        ans = 0
print(ans)