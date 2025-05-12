# import sys

def perm(index):
    global ans,find_num
    if index == len(board):
        if find_num == int(cmd[1]):
            print(f"{cmd[0]} {cmd[1]} = {ans}")
            return True
        find_num += 1
        return None
    for i in range(len(board)):
        if used[i] == False:
            used[i] = True
            return_ans = ans
            ans += board[i]
            a = perm(index+1)
            if a:
                return True
            ans = return_ans
            used[i] = False
while True:
    try:
        cmd = input().split()
        ans = ""
        board = cmd[0]
        used = [False] * (len(board)+1)
        find_num = 1
        a = perm(0)
        if not a:
            print(f"{cmd[0]} {cmd[1]} = No permutation")
        
    except EOFError:
        break