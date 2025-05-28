
import heapq
import sys
N = int(sys.stdin.readline().rstrip())
heap_list = []
for _ in range(N):
    heapq.heappush(heap_list,int(sys.stdin.readline().strip()))
ans = 0
if N != 1:
    while len(heap_list):
        first = heapq.heappop(heap_list)
        second = heapq.heappop(heap_list)
        ans += first + second
        if len(heap_list) == 0:
            break
        heapq.heappush(heap_list,first+second)
    print(ans)
else:
    print(0)