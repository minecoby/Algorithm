import sys
from heapq import heappush, heappop

V,E = map(int,sys.stdin.readline().split())
K = int(input())

path = {}
for i in range(1, V+1):
    path[i] = []
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    path[u].append([w,v])
distance = [float("inf")] * (V+1)
distance[K] = 0

heap_list = []
heappush(heap_list,(0,K))
while heap_list:
    weight,vertex = heappop(heap_list)
    if weight == distance[vertex]:
        for i in path[vertex]:
            new_weight = i[0] + weight
            if distance[i[1]] > new_weight:
                distance[i[1]] = new_weight
                heappush(heap_list,(new_weight,i[1]))
for ans in distance[1:]:
    print(ans if ans != float("inf") else "INF")
