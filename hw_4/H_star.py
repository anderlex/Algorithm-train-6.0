from collections import defaultdict, deque

def solve(n):
    stack = [(1, -1, 0)]  
    while stack:
        node, parent, state = stack.pop()
        if state == 0:
            stack.append((node, parent, 1))  
            for neighbor in tree[node]:
                if neighbor != parent:
                    stack.append((neighbor, node, 0))  
        elif state == 1:  
            dp[node][1] = costs[node]
            dp[node][0] = 0
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                dp[node][0] += dp[neighbor][1]
                dp[node][1] += min(dp[neighbor][0], dp[neighbor][1])

    if n == 1:
        print(dp[1][1], 1)
        print(1)
    else: 
        stack = deque([(1, -1, 1 if dp[1][1] < dp[1][0] else 0)])
        selected = []
        while stack:
            node, parent, take = stack.pop()
            if take == 1:
                selected.append(node)
            for neighbor in tree[node]:
                if neighbor == parent:
                    continue
                if take == 1:
                    if dp[neighbor][0] < dp[neighbor][1]:
                        stack.append((neighbor, node, 0))
                    else:
                        stack.append((neighbor, node, 1))
                else:
                    stack.append((neighbor, node, 1))
        if dp[1][0] < dp[1][1]:
            cost = dp[1][0]
        else:
            cost = dp[1][1]
        print(cost, len(selected))
        print(*selected)

n = int(input())
tree = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

costs = [0] + list(map(int, input().split()))
dp = [[0, 0] for _ in range(n + 1)]

solve(n)

