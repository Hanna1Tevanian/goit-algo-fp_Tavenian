import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4()) 

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) 
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Обхід дерева у глибину (DFS) з візуалізацією
def dfs_with_visualization(node, visited=set()):
    if node is None:
        return

    print("Visited Node:", node.val)

    node.color = "#%02x%02x%02x" % (255 - len(visited), 100, 100 + len(visited) * 10)  
    visited.add(node)

    draw_tree(root)  

    if node.left and node.left not in visited:
        dfs_with_visualization(node.left, visited)
    if node.right and node.right not in visited:
        dfs_with_visualization(node.right, visited)

# Обхід дерева у ширину (BFS) з візуалізацією
def bfs_with_visualization(root):
    if root is None:
        return

    queue = [root]
    visited = set()

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print("Visited Node:", node.val)

            node.color = "#%02x%02x%02x" % (255 - len(visited), 100, 100 + len(visited) * 10)  
            visited.add(node)

            draw_tree(root)  

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)

# Виклик обходу у глибину з візуалізацією
print("DFS Traversal:")
dfs_with_visualization(root)

# Виклик обходу у ширину з візуалізацією
print("BFS Traversal:")
bfs_with_visualization(root)
