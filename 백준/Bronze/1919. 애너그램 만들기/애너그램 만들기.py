def find(a,b):
    t = b[:]
    for i in b:
        if i in a:
            a.remove(i)
            t.remove(i)
    return len(a)+len(t)


a = list(input())
b = list(input())

print(find(a,b))