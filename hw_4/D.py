import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None
        
class Tree:
    def __init__(self):
        self.root = None    
            
    def add_node(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            print("DONE")
            return
        
        cur = self.root
        while True:
            if cur.value < value:
                if cur.right is None:
                    cur.right = TreeNode(value)
                    print("DONE")
                    return
                cur = cur.right
            elif cur.value > value:
                if cur.left is None:
                    cur.left = TreeNode(value)
                    print("DONE")
                    return
                cur = cur.left
            else:
                print("ALREADY")
                return
        
    def find_node(self, value):
        cur = self.root
        while cur:
            if cur.value == value:
                print("YES")
                return
            elif cur.value < value:
                cur = cur.right
            else:
                cur = cur.left
        print("NO")
        return

    def print_tree(self):
        def dfs(node, level=0):
            if node is not None:
                dfs(node.left, level + 1)
                print("." * level + str(node.value))
                dfs(node.right, level + 1)
        dfs(self.root)

binary_tree = Tree()

for line in sys.stdin:
    req = line.split()
    if req[0] == 'ADD':
        binary_tree.add_node(int(req[1]))
    elif req[0] == 'SEARCH':
        binary_tree.find_node(int(req[1]))
    else:
        binary_tree.print_tree()