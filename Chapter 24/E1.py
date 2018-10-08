class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


def print_list(node):
    print("[", end="")
    while node is not None:
        if node.next is not None:
            print(node, end=", ")
        else:
            print(node, end="")
        node = node.next
    print("]")


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
print_list(node1)
