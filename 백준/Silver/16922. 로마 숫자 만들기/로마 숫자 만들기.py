N = int(input())
board = [1,5,10,50]
ans = set()
cnt = 0
def lome(k, index):
    global cnt
    if k == N:
        ans.add(cnt)
        return
    for i in range(index,4):
        cnt += board[i]
        lome(k+1,i)
        cnt -= board[i]
lome(0,0)
print(len(ans))