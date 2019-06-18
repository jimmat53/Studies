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

  def append(self, value):
    """Append a node to a LinkedList."""
    new_node = Node(value)
    if self.head:
      node = self.head
      while node.next:
        node = node.next
      node.next = new_node
    else:
      self.head = new_node

  def print_list(self, this_node):
    """Print the Linkedlist recursively."""
    if not this_node:
      return
    else:
      print(this_node.data)
      self.print_list(this_node.next)

  def reverse_list(self):
    """Reverse the Linkedlist object."""
    prev = current = self.head
    while current:
      tmp = current.next
      current.next = prev
      prev = current
      current = tmp
    self.head.next = None
    self.head = prev        

  def delete(self, ele):
    """Delete an element in the Linkedlist."""
    prev = current = self.head
    while current:
      if current.data == ele:
        if current == self.head:
          self.head = self.head.next
          return
        else:
          prev.next = current.next
      prev = current
      current = current.next

  def search(self, ele):
    """Search for an element in the Linkedlist."""

  def insert_middle(self, ele, position):
    """Insert an element at the nth position in the Linkedlist."""

  def remove_nth_element(self, position):
    """Remove an element at the nth position in the Linkedlist."""

  def length(self):
    """Find the length of the Linkedlist."""
    count = 0
    current = self.head
    while(current):
      count+=1
      current = current.next
    return count
    

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
  LIST_ONE.append(4)
  print('Linked List=>')
  LIST_ONE.print_list(LIST_ONE.head)

  LIST_ONE.reverse_list()
  print('Reversed Linked List=>')
  LIST_ONE.print_list(LIST_ONE.head)
    
  print('Delete an element from Linked List=>')
  LIST_ONE.delete(3)
  LIST_ONE.delete(1)
  LIST_ONE.print_list(LIST_ONE.head)

  print('Length of the Linked List=>')
  print(LIST_ONE.length())
