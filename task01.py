
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    @classmethod
    def from_iterable(cls, values):
        llist = cls()
        for v in values:
            llist.insert_at_end(v)
        return llist

    def to_list(self):
        result, cur = [], self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    def print_list(self):
        print(" -> ".join(map(str, self.to_list())) or "(порожній)")

# ---------- 1. Реверсування (зміна посилань між вузлами) ----------
def reverse_list(llist: LinkedList) -> LinkedList:
    prev, cur = None, llist.head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    llist.head = prev
    return llist

# ---------- 3. Злиття двох відсортованих ланцюжків вузлів ----------
def _merge_nodes(a: Node, b: Node) -> Node:
    dummy = Node()
    tail = dummy
    while a and b:
        if a.data <= b.data:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a if a else b
    return dummy.next


def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    merged = LinkedList()
    merged.head = _merge_nodes(list1.head, list2.head)
    list1.head = list2.head = None
    return merged


# ---------- 2. Сортування злиттям ----------
def _split(head: Node):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    middle = slow.next
    slow.next = None
    return head, middle


def _merge_sort_nodes(head: Node) -> Node:
    if head is None or head.next is None:
        return head
    left, right = _split(head)
    return _merge_nodes(_merge_sort_nodes(left), _merge_sort_nodes(right))


def merge_sort(llist: LinkedList) -> LinkedList:
    llist.head = _merge_sort_nodes(llist.head)
    return llist


if __name__ == "__main__":
    llist = LinkedList.from_iterable([5, 3, 10, 1, 8, 2])
    print("Початковий список:")
    llist.print_list()

    reverse_list(llist)
    print("\nРеверсований список:")
    llist.print_list()

    merge_sort(llist)
    print("\nВідсортований список (merge sort):")
    llist.print_list()

    a = LinkedList.from_iterable([1, 4, 7, 9])
    b = LinkedList.from_iterable([2, 3, 8, 11, 12])
    print("\nСписок A:", end=" ")
    a.print_list()
    print("Список B:", end=" ")
    b.print_list()
    merged = merge_sorted_lists(a, b)
    print("Об'єднаний відсортований список:")
    merged.print_list()
