n = int(input())
for i in range (1,n+1,1):
    total = 0
    total = int(((i*i)*((i*i) -1))/2)
    a = i - 2
    b = i - 1 
    attack = a * b * 4
    print(total-attack)
    