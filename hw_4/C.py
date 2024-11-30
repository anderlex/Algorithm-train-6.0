import sys

def ancestors(child, tree):
    result = []
    result.append(child)
    while child in tree:
        child = tree[child]
        result.append(child)
    return result

tree = dict()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    tree[child] = parent


for line in sys.stdin:
    u, v = line.split()
    ancestors_for_1 = set(ancestors(u, tree))
    for ancestor in ancestors(v, tree):
        if ancestor in ancestors_for_1:
            print(ancestor)
            break