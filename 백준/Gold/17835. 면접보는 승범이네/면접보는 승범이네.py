from heapq import heappush, heappop
import sys

def dijkstra():
    distance = [float("inf")] * (N+1)
    heap_list = []
    for t in station:
        heappush(heap_list,(0,t))
        distance[t] = 0
    while heap_list:
        weight, vertex = heappop(heap_list)
        if distance[vertex] != weight: continue
        for info in path[vertex]:
            new_weight = weight + info[0]
            if distance[info[1]] > new_weight:
                distance[info[1]] = new_weight
                heappush(heap_list,(new_weight,info[1]))
    return distance

N,M,K = map(int,sys.stdin.readline().split())
path = {}
for i in range(1,N+1):
    path[i] = []

for _ in range(M):
    u,v,c = map(int,sys.stdin.readline().split())
    path[v].append([c,u])

station = list(map(int,sys.stdin.readline().split()))

ending = float("inf")
end_distance = 0
ans = dijkstra()
for i in range(1,len(ans)):
    if end_distance < ans[i]:
        ending = i
        end_distance = ans[i]
print(ending)
print(end_distance)
        