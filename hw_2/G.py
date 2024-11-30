n, c = map(int, input().split())
s = input()

i = 0
ans = 0
count = 0
count_a = 0
count_b = 0
for j in range(n):
    if s[j] == 'a':
        count_a += 1
    elif s[j] == 'b':
        count_b += 1
        if count_a != 0:
            count += count_a
    while count > c and i <= j:
        if s[i] == 'a':
            count -= count_b
            count_a -= 1
        elif s[i] == 'b' and count_b > 1:
            count_b -= 1
        i += 1
    ans = max(ans, j - i + 1)

print(ans)