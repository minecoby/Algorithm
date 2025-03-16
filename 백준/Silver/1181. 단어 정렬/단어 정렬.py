N = int(input())
array = []
for _ in range(N):
    array.append(input())
array = list(set(array))
sorted_list = sorted(array,key= lambda x : (len(x), x))
for i in sorted_list:
    print(i)