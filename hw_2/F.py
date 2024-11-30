n = int(input())
a = list(map(int, input().split()))

mod = 1000000007

ans = 0
pair_sum = 0
cur_sum = a[0]

for i in range(2, n):
    pair_sum += cur_sum * a[i - 1]
    cur_sum += a[i - 1]
    ans += pair_sum * a[i] % mod
    ans %= mod

print(ans)