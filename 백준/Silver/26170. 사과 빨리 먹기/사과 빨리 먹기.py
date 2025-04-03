loc_x = [1,0,-1,0]
loc_y = [0,1,0,-1]
result = float('inf')

def dfs(arr, r, c, cnt, apple_cnt):
    global result

    if apple_cnt == 3:
        result = min(result, cnt)
        return 
    temp = arr[r][c]
    arr[r][c] = -1  

    for i in range(4):
        nx, ny = r + loc_x[i], c + loc_y[i]

        if 0 <= nx < 5 and 0 <= ny < 5 and arr[nx][ny] != -1:
            if arr[nx][ny] == 1:  
                dfs(arr, nx, ny, cnt + 1, apple_cnt + 1)
            else:  
                dfs(arr, nx, ny, cnt + 1, apple_cnt)

    arr[r][c] = temp


arr = [list(map(int,input().split())) for _ in range(5)]
r,c = map(int,input().split())
dfs(arr,r,c,0,0)
print(result if result != float('inf') else -1)