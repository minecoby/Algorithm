N,M = map(int,input().split())

password = {}

for i in range(N):
    cmd = input().split()
    password[cmd[0]] = cmd[1]
for i in range(M):
    print(password[input()])