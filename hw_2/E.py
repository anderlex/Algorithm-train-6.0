n = int(input())
a = list(map(int, input().split()))

a.sort()
l = (n - 1) // 2
r = n // 2

if l == r:
    print(a[l], end=' ')
    l -= 1
    r += 1
while r < n and l > -1:
    print(a[l], end=' ')
    l -= 1
    print(a[r], end=' ')
    r += 1

        