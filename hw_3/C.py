n, k = map(int, input().split())
a = list(map(int, input().split()))

result = []
deque = []

for i in range(n):
    if deque and deque[0] < i - k + 1:
        deque.pop(0)

    while deque and a[deque[-1]] > a[i]:
        deque.pop()

    deque.append(i)

    if i >= k - 1:
        print(a[deque[0]])