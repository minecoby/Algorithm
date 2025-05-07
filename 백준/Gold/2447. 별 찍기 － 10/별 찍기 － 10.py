
def draw(n):
    if n == 1:
        return "*"
    towers = draw(n//3)
    L = []
    for tower in towers:
        L.append(tower*3)
    for tower in towers:
        L.append(tower + ' '* (n//3) + tower)
    for tower in towers:
        L.append(tower*3)
    return L
   
        
N = int(input())
ans = draw(N)
for i in ans:
    print(i)


    