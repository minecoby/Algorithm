
import heapq
import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    heap_list = list(map(int,sys.stdin.readline().split()))
    heapq.heapify(heap_list)
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