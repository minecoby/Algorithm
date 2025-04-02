loc_x = [1,0,-1,0]
loc_y = [0,1,0,-1]
result = 0

def dfs(arr,r,c,cnt,apple_cnt):
    global result
    if cnt <= 3 and apple_cnt >= 2:
        result = 1
        return
    if cnt > 3:
        return
    for i in range(4):
        nx,ny = r + loc_x[i] , c + loc_y[i]
        if 0 <= nx < 5 and 0 <= ny < 5 and arr[nx][ny] != -1:
            original = arr[nx][ny]  
            arr[r][c] = -1 
            if original == 1:
                dfs(arr, nx, ny, cnt + 1, apple_cnt + 1)
            else:
                dfs(arr, nx, ny, cnt + 1, apple_cnt)
            arr[r][c] = original

arr = [list(map(int,input().split())) for _ in range(5)]
r,c = map(int,input().split())
dfs(arr,r,c,0,0)
print(result)



