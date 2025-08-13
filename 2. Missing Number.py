n = int(input())
l = list(map(int,input().split()))
expected_sum = (n * (n + 1)) // 2
actual_sum = sum(l)

print(expected_sum - actual_sum)