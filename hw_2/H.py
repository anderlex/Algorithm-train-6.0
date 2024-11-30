# import random
# import time

# def generate(n):
#     return [random.randint(1, 1000000000) for i in range(n)]

# n = 200000
# a = generate(n)


n = int(input())
a = list(map(int, input().split()))

cur_sum = 0
total_sum = sum(a)

for i in range(1, n):
    cur_sum += i * a[i]

ans = cur_sum
prefix_sum = 0

for i in range(n):
    prefix_sum += a[i]
    cur_sum += prefix_sum - (total_sum - prefix_sum)
    ans = min(ans, cur_sum)

print(ans)