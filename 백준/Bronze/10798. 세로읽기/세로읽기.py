lines= []

for i in range(5):
    lines.append(list(input()))
max_len = max(len(line) for line in lines)

result = ""

for i in range(max_len):
    for line in lines:
        if i < len(line):  
            result += line[i]

print(result)
