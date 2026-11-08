
import heapq
import uuid

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color #колір вузла
        self.id = str(uuid.uuid4()) #унікальний ідентифікатор вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def _label_color(color):
    r, g, b = mcolors.to_rgb(color)
    return "black" if 0.299 * r + 0.587 * g + 0.114 * b > 0.6 else "white"


def draw_tree(tree_root, title=None, ax=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    show = ax is None
    if show:
        plt.figure(figsize=(8, 5))
        ax = plt.gca()
    ax.clear()
    nx.draw(tree, pos=pos, arrows=False, node_size=2500, node_color=colors, ax=ax)

    for node_id, data in tree.nodes(data=True):
        nx.draw_networkx_labels(tree, pos, labels={node_id: labels[node_id]}, ax=ax,
                                font_weight="bold", font_color=_label_color(data["color"]))
    if title:
        ax.set_title(title)
    if show:
        plt.show()


def heap_to_tree(heap, index=0):
    if index >= len(heap):
        return None
    node = Node(heap[index])
    node.left = heap_to_tree(heap, 2 * index + 1)
    node.right = heap_to_tree(heap, 2 * index + 2)
    return node


def draw_heap(heap, title="Бінарна купа"):
    if not heap:
        print("Купа порожня")
        return
    draw_tree(heap_to_tree(heap), title=title)


if __name__ == "__main__":
    data = [10, 4, 7, 1, 15, 3, 9, 2, 8, 5]
    heap = data[:]
    heapq.heapify(heap)  # min-heap
    print("Вхідні дані:", data)
    print("Купа (масив):", heap)
    draw_heap(heap, title="Min-heap")
