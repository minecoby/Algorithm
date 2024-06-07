import sys

n = int(input())
result = set()
for i in range(n):
    people = sys.stdin.readline().split()
    if people[1] == "enter":
        if people[0] not in result:
            result.add(people[0])
    if people[1] == "leave":
        if people[0] in result:
            result.remove(people[0])
result = list(result)
result.sort(reverse=True)
for i in result:
    print(i)