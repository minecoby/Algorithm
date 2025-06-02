import sys
from heapq import heappush, heappop

V = int(sys.stdin.readline().rstrip())
E = int(sys.stdin.readline().rstrip())

path = {}
for i in range(1, V+1):
    path[i] = []
for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    path[u].append([w,v])
distance = [float("inf")] * (V+1)
S,E = map(int,sys.stdin.readline().split())
distance[S] = 0
walk = [0] * (V+1)

heap_list = []
heappush(heap_list,(0,S))
while heap_list:
    weight,vertex = heappop(heap_list)
    if weight != distance[vertex]: continue
    for i in path[vertex]:
        new_weight = i[0] + weight
        if distance[i[1]] > new_weight:
            distance[i[1]] = new_weight
            walk[i[1]] = vertex 
            heappush(heap_list,(new_weight,i[1]))
print(distance[E])
ans = []
cur = E
while cur != S:
    ans.append(walk[cur])
    cur = walk[cur]

print(len(ans)+1)
ans.reverse()
print(*ans,E)
