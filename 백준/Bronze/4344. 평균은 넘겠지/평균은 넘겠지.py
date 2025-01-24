C = int(input())
for _ in range(C):
    result = list(map(int,input().split()))
    avg = sum(result[1:])/result[0]
    count = len([x for x in result[1:] if x > avg])
    print(f"{count/result[0]*100:.3f}%")