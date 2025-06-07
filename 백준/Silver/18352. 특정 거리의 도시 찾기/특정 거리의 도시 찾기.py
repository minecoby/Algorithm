import sys
from heapq import heappush, heappop

def dijkstra(start):
    heap_list = []
    heappush(heap_list,(0,start))
    distance[start] = 0
    while heap_list:
        weight, vertex = heappop(heap_list)
        if distance[vertex] != weight: continue
        for info in path[vertex]:
            new_weight = weight + info[0]
            if distance[info[1]] > new_weight:
                distance[info[1]] = new_weight
                if on[info[1]] == True:
                    heappush(heap_list,(new_weight,info[1]))
    return distance

N,M,K,X = map(int,sys.stdin.readline().split())
path = {}
distance = [float("inf")] * (N+1)
on = [False] * (N+1)
for i in range(1,N+1):
    path[i] = []

for i in range(M):
    A,B = map(int,sys.stdin.readline().split())
    path[A].append([1,B])
    on[A] = True


result = dijkstra(X)
is_ans = False
for index,data in enumerate(result):
    if data == K:
        is_ans = True
        print(index)
if not is_ans:
    print(-1)

