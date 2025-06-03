import sys
from heapq import heappop,heappush


def dijkstra(start,end):
    distance = [float("inf")]*(N+1)
    heap_list = []
    heappush(heap_list,(0,start))
    distance[start] = 0
    while heap_list:
        weight,vertex = heappop(heap_list)
        if weight != distance[vertex]: continue
        for info in path[vertex]:
            new_weight = weight + info[0]
            if distance[info[1]] > new_weight:
                distance[info[1]] = new_weight
                heappush(heap_list,(new_weight,info[1]))
    return distance[end]
            
    
N,E = map(int,sys.stdin.readline().split())
path = {}
for i in range(1,N+1):
    path[i] = []
for i in range(E):
    a,b,c = map(int,sys.stdin.readline().split())
    path[a].append([c,b])
    path[b].append([c,a])

v1,v2 = map(int,sys.stdin.readline().split())

ans = min(dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,N), dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,N))
if ans >= float("inf"):
    print(-1)
else:
    print(ans)