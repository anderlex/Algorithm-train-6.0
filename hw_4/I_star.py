from collections import defaultdict
import sys
sys.setrecursionlimit(100000)

def dfs(node, parent, dist):
    farthest_node = node
    max_dist = dist
    for neighbor in graph[node]:
        if neighbor != parent:
            next_node, next_dist = dfs(neighbor, node, dist + 1)
            if next_dist > max_dist:
                farthest_node = next_node
                max_dist = next_dist
    return farthest_node, max_dist

def dfs_skip_edge(node, parent, dist, edge):
    farthest_node = node
    max_dist = dist
    for neighbor in graph[node]:
        if neighbor != parent:
            if (neighbor, node) == edge or (node, neighbor) == edge:
                continue
            next_node, next_dist = dfs_skip_edge(neighbor, node, dist + 1, edge)
            if next_dist > max_dist:
                farthest_node = next_node
                max_dist = next_dist
    return farthest_node, max_dist

def find_path(start, end):
    parent = {start: None}
    stack = [(start, -1)]
    while stack:
        node, prev = stack.pop()
        if node == end:
            break
        for neighbor in graph[node]:
            if neighbor != prev and neighbor not in parent:
                parent[neighbor] = node
                stack.append((neighbor, node))
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    return path

n = int(input())
graph = defaultdict(list)
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

diameter_u, _ = dfs(1, -1, 0)
diameter_v, length_diameter = dfs(diameter_u, -1, 0)
diameter = find_path(diameter_u, diameter_v)
diameter_set = set(diameter)
path_diameters = [0] * (n + 1)
path_depth = [0] * (n + 1)

max_product = 0
k = 0
for node in diameter:
    max_depth = 0
    max_diameter = 0
    if node == diameter_u or node == diameter_v:
        continue
    if len(graph[node]) == 2:
        max_product = max(max_product, k * (length_diameter - k))
    else:
        for child in graph[node]:
            if child not in diameter_set:
                far_child, child_depth = dfs(child, node, 0)
                _, child_diameter = dfs_skip_edge(far_child, -1, 0, (node, child))
                max_depth = max(max_depth, child_depth + 1)
                max_diameter = max(max_diameter, child_diameter)
    path_diameters[node] = max_diameter
    path_depth[node] = max_depth

max_path_left = [0] * (n + 1)
max_path_right = [0] * (n + 1)

for i in range(1, length_diameter):
    max_path_left[diameter[i]] = max(
        i,
        i + path_depth[diameter[i]],
        max_path_left[diameter[i - 1]]
        )

for i in range(length_diameter - 1, 0, -1):
    max_path_right[diameter[i]] = max(
        length_diameter - i,
        length_diameter - i + path_depth[diameter[i]],
        max_path_right[diameter[i + 1]]
        )

for i in range(1, length_diameter):
    max_product = max(
        max_product,
        path_diameters[diameter[i]] * length_diameter,
        max_path_left[diameter[i]] * max_path_right[diameter[i + 1]]
    )

print(max_product)