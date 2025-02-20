angles = []
name = ["Equilateral","Isosceles","Scalene"]
for _ in range(3):
    angles.append(int(input()))
if sum(angles) != 180:
    print("Error")
else:
    print(name[len(set(angles))-1])