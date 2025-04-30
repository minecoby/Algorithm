num = [1 for _ in range(10)]
count = 1
n = input().strip()
for i in n:
    nn = int(i)
    if num[nn] >= 1:
        num[nn] -= 1
    elif nn == 6 and num[9] >= 1:
        num[9] -= 1
    elif nn == 9 and num[6] >= 1:
        num[6] -= 1
    else:
        count += 1
        for j in range(10):
            num[j] += 1
        num[nn] -= 1
print(count)