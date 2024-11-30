n, b = map(int, input().split())
a = list(map(int, input().split()))

wait = 0
ans = 0
for t in range(n):
    if a[t] > b:
        wait += a[t] - b
        ans += b + wait
    else:
        ans += a[t] + wait
        if wait > (b - a[t]):
            wait -= (b - a[t])
        else:
            wait = 0

print(ans + wait)