N,M = map(int,input().split())
while( N > (M*2)) :
    N = N - (M*2)
b = []
c = []
for i in range(M):
    a= list((map(int,input().split())))
    b.append(a)
    c+= a

c.sort()
o = c[N-1]


for i in range(len(b)):
    if o in b[i]:
        print(i+1)

