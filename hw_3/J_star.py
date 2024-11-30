n, H = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))

chairs = [(h[i], w[i]) for i in range(n)]
chairs.sort()

if n == 1:
    print(0)
else:
    ans = 10**11
    l = 0
    width = 0
    deque = []
    for r in range(n):
        width += chairs[r][1]
        if r > 0:
            while deque and (chairs[r][0] - chairs[r - 1][0] > deque[-1]):
                deque.pop()
            deque.append(chairs[r][0] - chairs[r - 1][0])
        while width >= H:
            if deque:
                ans = min(ans, deque[0])
            else:
                ans = 0
                break
            width -= chairs[l][1]
            l += 1
            if deque and deque[0] == (chairs[l][0] - chairs[l - 1][0]):
                deque.pop(0) 
    print(ans)