n, k = map(int, input().split())
d = list(map(int, input().split()))

r = 0
ans = 0
for l in range(n):
    while r < n and d[r] - d[l] <= k:
        r += 1
    ans += n - r
print(ans)