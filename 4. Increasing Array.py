n = int(input())
l = list(map(int,input().split()))

count = 0

for i in range(1,n,1):
    if l[i]<l[i-1]:
        count=count+l[i-1]-l[i]
        l[i]=l[i-1]
print(count)
