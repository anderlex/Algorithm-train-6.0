n = int(input())
a = list(map(int, input().split()))
m, k = map(int, input().split())
x = list(map(int, input().split()))

indeces = [1]
count = 0
l = 0

for i in range(1, n):
    if a[i - 1] > a[i]:
        l = i
        count = 0
    elif a[i - 1] == a[i]:
        count += 1
        while count > k and l < n:
            l += 1
            if a[l - 1] == a[l]:
                count -= 1
    indeces.append(l + 1)

for j in x:
    print(indeces[j - 1], end = ' ')