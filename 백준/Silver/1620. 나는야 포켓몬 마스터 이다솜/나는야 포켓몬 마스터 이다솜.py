N,M = map(int,input().split())

poke = {}

for i in range(N):
    poke[i] = input()

poke_reverse = {v:k for k,v in poke.items()}
for i in range(M):
    cmd = input()
    try:
        cmd = int(cmd)
        print(poke[cmd-1])
    except ValueError:
        print(poke_reverse[cmd]+1)
        


