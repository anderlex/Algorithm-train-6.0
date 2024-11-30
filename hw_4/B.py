from collections import defaultdict
import sys

sys.setrecursionlimit(100000)

def build_tree(node):
    return [node, [build_tree(child) for child in tree[node]]]

def calculate_children(node, children_dict):
    name, children = node
    count = 0
    for child in children:
        count += 1 + calculate_children(child, children_dict)
    children_dict[name] = count
    return count

n = int(input())
tree = defaultdict(list)
children = set()

for i in range(n - 1):
    child, parent = input().split()
    tree[parent].append(child)
    children.add(child)

root = next(node for node in tree.keys() if node not in children)
nested_tree = build_tree(root)

children_dict = {}
calculate_children(nested_tree, children_dict)
for name in sorted(children_dict.keys()):
    print(name, children_dict[name])