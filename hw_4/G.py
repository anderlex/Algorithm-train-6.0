from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

def modified_fact(answer, value):
    while value > 1:
        answer *= value
        value -= 1
        answer %= K
    return answer

def preprocessing():
    lonely = 0
    graph = defaultdict(list)
    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for v in range(1, n + 1):
        if not graph[v]:
            lonely += 1
    return graph, lonely

def BFS(graph, node, parent, component):
    visited.add(node)
    component.append(node)
    for child in graph[node]:
        if child != parent:
            if child in visited:
                return -1
            visited.add(child)
            count_subtrees[child] += 1
            if graph[child] == [node]:
                count_leaves[node] += 1
            else:
                count_subtrees[node] += 1
                if BFS(graph, child, node, component) == -1:
                    return -1
    return 0

def count_answer(answer):
    for k in range(lonely):
        answer *= (u + 2 + k)
        answer %= K
    for component in components:
        if len(component) == 1:
            value = count_leaves[component[0]]
            answer = modified_fact(answer, value)
            answer *= 2
        else:
            for root in component:
                value = count_leaves[root]
                answer = modified_fact(answer, value)
            answer *= 4
        answer %= K
    value = len(components)
    answer = modified_fact(answer, value)
    return answer

n, m, K = map(int, input().split())
graph, lonely = preprocessing()

count_leaves = defaultdict(int)
count_subtrees = defaultdict(int)

visited = set()
components = []
u = n - lonely

def solve():
    answer = 1
    for v in range(1, n + 1):
        if v not in visited and len(graph[v]) > 1:
            component = []
            if BFS(graph, v, -1, component) == -1:
                print(0)
                return
            components.append(component)
        elif v not in visited and len(graph[v]) == 1:
            if graph[v][0] not in visited and len(graph[graph[v][0]]) == 1:
                visited.add(v)
                visited.add(graph[v][0])
                components.append([v])
    for node, count in count_subtrees.items():
        if count > 2:
            print(0)
            return
    print(count_answer(answer))

solve()