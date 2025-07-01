L,N = [],[]
for _ in range(10):
    L.append(int(input()))
for i in range(10):
    N.append(L[i]%42)
print(len(set(N)))