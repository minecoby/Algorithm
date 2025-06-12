T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    print(f"Scenario #{i+1}:")
    print((b-a+1) * (a+b)//2)
    print()