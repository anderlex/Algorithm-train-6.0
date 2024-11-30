from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

def dfs(node, parent):
    subtree_size[node] = 1
    for neighbor in tree[node]:
        if neighbor != parent:
            dfs(neighbor, node)
            subtree_size[node] += subtree_size[neighbor]
    total_height[node] += subtree_size[node]
    if parent != -1:
        total_height[parent] += total_height[node]

n = int(input())
coaches = list(map(int, input().split()))
tree = {}

for i in range(1, n + 1):
    tree[i] = []

for i in range(n - 1):
    a, b = i + 2, coaches[i]
    tree[a].append(b)
    tree[b].append(a)

total_height = defaultdict(int)
subtree_size = defaultdict(int)
dfs(1, -1)
for v in range(1, n + 1):
    print(total_height[v], end = ' ')