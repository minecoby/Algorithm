N = int(input())
W = [list(map(int,input().split())) for _ in range(N)]

# 모든도시를 기점으로 출발? 0 -> 1  -> 2 -> 3 -> 0 방문 가능하면 weight 기록 
# 중간에 weight 가 0인경우가 존재하면? return
# 방문한 도시 다시 못가니깐 used 방문표시 시키기
# 방문 수 cnt 가 3이되면 항상 현재 인덱스에서 start인덱스로 방문시도, 되면 weight기록
# 안되면 return 

used = [False] * (N+1)
ans = []
def TSP(start, index, weight, cnt):
    global ans
    if cnt == N-1:
        if W[index][start] != 0:
            weight += W[index][start]
            ans.append(weight)
            return 
        return

    for i in range(N):
        if used[i] == False and W[index][i] != 0:
            used[i] = True
            weight += W[index][i]
            TSP(start,i,weight,cnt + 1)
            weight -= W[index][i]
            used[i] = False
        
for i in range(N):
    used[i] = True
    TSP(i,i,0,0)
    used[i] = False
print(min(ans))
