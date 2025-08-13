n = input()
n = n + 'H'
count = max_count = 1
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        count = count + 1
    else:
        max_count = max(max_count,count)
        count = 1
print(max_count)