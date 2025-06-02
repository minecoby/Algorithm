import sys
from heapq import heappush,heappop

def dijkstra(n):
    distance = [float("inf")] * (N+1)
    heap_list = []
    distance[n] = 0
    heappush(heap_list,(0,n))

    while heap_list:
        w,v = heappop(heap_list)
        if distance[v] != w: continue
        for info in path[v]:
            new_w = w + info[0]
            if distance[info[1]] > new_w:
                distance[info[1]] = new_w
                heappush(heap_list,(new_w,info[1]))
    return distance

N,M,X = map(int,sys.stdin.readline().split())
distance = [float("inf")] * (N+1)
path = {}
for i in range(1,N+1):
    path[i] = []
for _ in range(M):
    u,v,t = map(int,sys.stdin.readline().split())
    path[u].append([t,v])

endtostart = dijkstra(X)
ans = 0
for i in range(1,N+1):
    ans = max(ans, endtostart[i] + dijkstra(i)[X])
print(ans)