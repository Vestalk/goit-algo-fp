
from collections import deque

import matplotlib.pyplot as plt

from task04 import Node, draw_tree, heap_to_tree


def generate_colors(n, start="#0B2E59", end="#CFE8FF"):
    s = [int(start[i:i + 2], 16) for i in (1, 3, 5)]
    e = [int(end[i:i + 2], 16) for i in (1, 3, 5)]
    colors = []
    for k in range(n):
        t = k / (n - 1) if n > 1 else 0
        rgb = [round(s[c] + (e[c] - s[c]) * t) for c in range(3)]
        colors.append("#{:02X}{:02X}{:02X}".format(*rgb))
    return colors


def dfs_order(root):
    order, stack = [], [root] if root else []
    while stack:
        node = stack.pop()
        order.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order


def bfs_order(root):
    order, queue = [], deque([root] if root else [])
    while queue:
        node = queue.popleft()
        order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return order


def all_nodes(root):
    return bfs_order(root)


def visualize_traversal(root, traversal, name, delay=0.8):
    order = traversal(root)
    colors = generate_colors(len(order))

    for node in all_nodes(root):
        node.color = "#D3D3D3"

    fig, ax = plt.subplots(figsize=(9, 5.5))
    for step, (node, color) in enumerate(zip(order, colors), start=1):
        node.color = color
        draw_tree(root, title=f"{name}: крок {step}/{len(order)} — вузол {node.val} ({color})", ax=ax)
        plt.pause(delay)

    print(f"{name}:", " -> ".join(f"{n.val}({c})" for n, c in zip(order, colors)))
    draw_tree(root, title=f"{name}: порядок " + " → ".join(str(n.val) for n in order), ax=ax)
    plt.show()


if __name__ == "__main__":
    heap = [0, 4, 1, 5, 10, 3, 7, 12, 6]
    root = heap_to_tree(heap)

    visualize_traversal(root, dfs_order, "DFS (стек)")
    visualize_traversal(root, bfs_order, "BFS (черга)")
