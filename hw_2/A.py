n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(len(a)):
	ans += a[i]
	print(ans, end = ' ')