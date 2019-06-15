"""Singly LinkedList."""


class Node:
    """A node of a singly linked list."""

    def __init__(self, data):
        """Node constructor."""
        self.data = data
        self.next = None


class LinkedList():
    """LinkedList data structure and operations on it."""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """Append a node to a LinkedList."""
        new_node = Node(value)
        if self.head:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def print_list(self, this_node):
        """Print the Linkedlist recursively."""
        if not this_node:
            return
        else:
            print(this_node.data)
            self.print_list(this_node.next)

    def reverse_list(self):
        """Reverse the Linkedlist object."""

    def delete(self, ele):
        """Delete an element in the Linkedlist."""

    def search(self, ele):
        """Search for an element in the Linkedlist."""

    def insert_middle(self, ele, position):
        """Insert an element at the nth position in the Linkedlist."""

    def remove_nth_element(self, position):
        """Remove an element at the nth position in the Linkedlist."""

    def length(self):
        """Find the length of the Linkedlist."""

    def copy_list(self):
        """Return a copy of the Linkedlist object ."""

    def detect_loop(self):
        """Detect cycles in Linkedlist."""

    def sort(self):
        """Sort the Linkedlist."""

    def sum(self, list_1, list_2):
        """Sum of 2 Linkedlists."""

    def concatenate_sorted_lists(self, list_1, list_2):
        """Concatenate 2 sorted Linkedlists."""


if __name__ == "__main__":
    LIST_ONE = LinkedList()
    LIST_ONE.append(1)
    LIST_ONE.append(2)
    LIST_ONE.append(3)
    LIST_ONE.print_list(LIST_ONE.head)
