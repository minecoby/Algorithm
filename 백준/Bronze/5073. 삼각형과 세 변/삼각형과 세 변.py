while True:
    angles = list(map(int,input().split()))
    if angles == [0,0,0]:
        break
    if max(angles) >= sum(angles)-max(angles):
        print("Invalid")
    else:
        a = ["Equilateral", "Isosceles", "Scalene"]
        print(a[len(set(angles))-1])
