import sys
from heapq import heappop, heappush

input = sys.stdin.readline

V,E = map(int,input().split())
node = {i:[] for i in range(1,V+1)}
visited = [False] * (V+1)


for _ in range(E):
    A,B,C = map(int,input().split())
    node[A].append((B,C))
    node[B].append((A,C))

ans = 0
heap_list = []
visited[1] = True

for next_node, cost in node[1]:
    heappush(heap_list, (cost, next_node))

while heap_list:
    cost, cur_node = heappop(heap_list)
    if not visited[cur_node]:
        visited[cur_node] = True
        ans += cost
        for next_node, next_cost in node[cur_node]:
            if not visited[next_node]:
                heappush(heap_list, (next_cost, next_node))

print(ans)
