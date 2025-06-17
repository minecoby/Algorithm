from heapq import heappush, heappop
import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    max_heap = []
    min_heap = []
    visited = dict()
    idx = 0

    for _ in range(k):
        cmd = sys.stdin.readline().split()
        if cmd[0] == "I":
            num = int(cmd[1])
            heappush(max_heap, (-num, idx))
            heappush(min_heap, (num, idx))
            visited[idx] = True
            idx += 1

        elif cmd[0] == "D":
            if cmd[1] == "1":
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heappop(max_heap)
            elif cmd[1] == "-1":
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heappop(min_heap)

    if max_heap and min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")
