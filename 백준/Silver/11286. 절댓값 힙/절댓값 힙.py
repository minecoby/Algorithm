import heapq
import sys
N = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(N):
    cmd = int(sys.stdin.readline().rstrip())
    if cmd == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(cmd),cmd))
