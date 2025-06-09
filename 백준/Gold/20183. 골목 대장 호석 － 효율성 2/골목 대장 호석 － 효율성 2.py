from heapq import heappush, heappop
import sys
N,M,A,B,C = map(int,sys.stdin.readline().split())

def dijkstra():
    heap_list = []
    heappush(heap_list,(0,0,A)) #거리값, 수치심, 경로? 
    distance[A][1] = 0
    
    while heap_list:
        weight,max_weight,vertex = heappop(heap_list)
        if distance[vertex][1] != weight: continue
        for info in path[vertex]:
            new_weight = weight + info[0]
            max_weight = max(max_weight,info[0])
            if new_weight > C: continue
            if distance[info[1]][0] <= max_weight:continue
            distance[info[1]][0] = max_weight
            distance[info[1]][1] = new_weight
            heappush(heap_list,(new_weight,max_weight,info[1]))
    return distance[B][0] if distance[B][1] != float("inf") else -1
                
path = {}
for i in range(1,N+1):
    path[i] = []
distance = [[float("inf"),float("inf")] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,sys.stdin.readline().split())
    path[u].append([w,v])
    path[v].append([w,u])

ans = dijkstra()
print(ans)
