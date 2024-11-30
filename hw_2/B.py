N, K = map(int, input().split())
num = list(map(int, input().split()))
sum_num = {0: 1}
cur = 0
ans = 0
for i in range(N):
    cur += num[i]
    if cur - K in sum_num:
        ans += sum_num[cur - K]
    if cur in sum_num:
        sum_num[cur] += 1
    else: sum_num[cur] = 1
print(ans)