A = list(input())
B = list(input().split())

for i in range(len(A)):
    if A[i] in B:
        A[i] = A[i].lower()
for i in A:
    print(i,end="")