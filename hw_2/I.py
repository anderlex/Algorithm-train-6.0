n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = list(map(int, input().split()))

algorithms = []
for i in range(n):
    algorithms.append((a[i], b[i], i + 1))

int_algos = sorted(
    algorithms,
    key=lambda x: (-x[0], -x[1], x[2])
)
use_algos = sorted(
    algorithms,
    key=lambda x: (-x[1], -x[0], x[2])
)

learned = set()
ans = []

i, u = 0, 0
for mood in p:
    if mood:
        while use_algos[u] in learned:
            u += 1
        print(use_algos[u][2], end = ' ')
        learned.add(use_algos[u])
        u += 1
    else:
        while int_algos[i] in learned:
            i += 1
        print(int_algos[i][2], end = ' ')
        learned.add(int_algos[i])
        i += 1