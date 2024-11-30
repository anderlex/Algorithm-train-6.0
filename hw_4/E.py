import sys
sys.setrecursionlimit(200000)

def dfs(node, parent):
    subtree_size[node] = 1
    for neighbor in tree[node]:
        if neighbor != parent:
            dfs(neighbor, node)
            subtree_size[node] += subtree_size[neighbor]

tree = dict()
answer = dict()
n = int(input())
for i in range(1, n + 1):
    tree[i] = []

for i in range(n - 1):
    parent, child = map(int, input().split())
    tree[parent].append(child)
    tree[child].append(parent)

'''
        1
      /
    4
  /   \       
3       5
      /
    2
'''

subtree_size = dict()
dfs(1, -1)
for v in range(1, n + 1):
    print(subtree_size[v], end = ' ')
