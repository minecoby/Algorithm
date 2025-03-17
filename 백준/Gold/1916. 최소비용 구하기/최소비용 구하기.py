import sys


N = int(sys.stdin.readline())  
M = int(sys.stdin.readline())  


graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))  

start, end = map(int, sys.stdin.readline().split())

INF = float("inf")
cnt = [INF] * (N + 1)  
cnt[start] = 0  

traveled = [False] * (N + 1)


for _ in range(N):
    min_node = -1
    min_value = INF
    for i in range(1, N + 1):
        if not traveled[i] and cnt[i] < min_value:
            min_node = i
            min_value = cnt[i]

    if min_node == -1:
        break


    traveled[min_node] = True


    for next_node, weight in graph[min_node]:
        if cnt[next_node] > cnt[min_node] + weight:
            cnt[next_node] = cnt[min_node] + weight  


print(cnt[end] if cnt[end] != INF else -1)

