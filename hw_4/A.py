from collections import defaultdict

def build_tree(node):
    return [node, [build_tree(child) for child in tree[node]]]

def calculate_heights(node, height, heights_dict):
    name, children = node
    heights_dict[name] = height
    for child in children:
        calculate_heights(child, height + 1, heights_dict)

n = int(input())
tree = defaultdict(list)
children = set()

for i in range(n - 1):
    child, parent = input().split()
    tree[parent].append(child)
    children.add(child)

root = next(node for node in tree.keys() if node not in children)
nested_tree = build_tree(root)

heights = {}
calculate_heights(nested_tree, 0, heights)
for name in sorted(heights.keys()):
    print(name, heights[name])