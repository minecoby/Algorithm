n = int(input())
k = int(input())
used = [False] * n
board = []
for i in range(n):
    board.append(input())
arr = []
ans = []
def card(a):
    global ans
    if a == k:
        m = ""
        for i in arr:
            m += i
        ans.append(m)
    
    for i in range(n):
        if used[i] == False:
            arr.append(board[i])
            used[i] = True
            card(a+1)
            arr.pop()  
            used[i] = False
card(0)
print(len(set(ans)))