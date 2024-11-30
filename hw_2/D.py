n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
l = 0
r = 0
min_days = 0
while l < n:
    while r < n and a[r] - a[l] <= k:
        r += 1
    min_days = max(min_days, r - l)
    l += 1

print(min_days)
