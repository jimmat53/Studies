"""Singly LinkedList."""

class LinkedListException(Exception):
  pass


class Node:
  """A node of a singly linked list."""

  def __init__(self, data):
    """Node constructor."""
    self.data = data
    self.next = None

  def __repr__(self):
    return 'Data: {}, Next(ObjID): {}'.format(str(self.data), str(id(self.next)))

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
    current = self.head
    while current:
      if current.data == ele:
        return True
      current = current.next
    return False

  def insert_middle(self, ele, position):
    """Insert an element at the nth position in the Linkedlist."""
    if position == 0 and self.length() == 0:
      new_node = Node(ele)
      self.head = new_node
    elif position > self.length():
      raise LinkedListException
    else:
      current = self.head
      prev = self.head
      counter = 0
      while current and counter < position:
        counter += 1
        prev = current
        current = current.next
      new_node = Node(ele)
      new_node.next = current
      if counter == 0:
        self.head = new_node
      else:
        prev.next = new_node

  def remove_nth_element(self, position):
    """Remove an element at the nth position in the Linkedlist."""
    if position > self.length() -1:
      raise LinkedListException
    else:
      current = self.head
      prev = self.head
      counter = 0
      while current and counter < position:
        counter += 1
        prev = current
        current = current.next
      if counter == 0:
        self.head = current.next
      else:
        prev.next = current.next

  def length(self):
    """Find the length of the Linkedlist."""
    count = 0
    current = self.head
    while(current):
      count+=1
      current = current.next
    return count
    
  def return_last_node(self):
    """Return the last node of the list."""
    if self.head:
      current = self.head
      while current:
        prev = current
        current = current.next
      return prev
    else:
      return None

  def copy_list(self):
    """Return a copy of the Linkedlist object ."""
    LIST_COPY = LinkedList()
    current = self.head
    while current:
      LIST_COPY.append(current.data)
      current = current.next
    return LIST_COPY

  def detect_loop(self):
    """Detect cycles in Linkedlist."""
    tortoise = self.head
    hare = self.head
    while hare:
      tortoise = tortoise.next
      hare = hare.next
      if hare:
        hare = hare.next  #Advance twice
      if tortoise == hare:
        return True
    return False


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
  LIST_ONE.reverse_list()
    
  print('Delete an element from Linked List=>')
  LIST_ONE.delete(3)
  LIST_ONE.delete(1)
  print('Linked List=>')
  LIST_ONE.print_list(LIST_ONE.head)

  print('Length of the Linked List=>')
  print(LIST_ONE.length())

  print('If element is present=>')
  print(LIST_ONE.search(2))
  print(LIST_ONE.search(100))
  
  print('Insert in the middle of the Linked List=>')
  LIST_ONE.insert_middle(0, 0)
  LIST_ONE.insert_middle(1, 1)
  LIST_ONE.insert_middle(3, 3)
  print('Linked List=>')
  LIST_ONE.print_list(LIST_ONE.head)

  try:
    LIST_ONE.insert_middle(100, 100)
  except LinkedListException:
    print('Invalid position')

  print('Removing element-4 from Linked List=>')
  LIST_ONE.remove_nth_element(4)
  LIST_ONE.print_list(LIST_ONE.head)
  print('Removing element-2 from Linked List=>')
  LIST_ONE.remove_nth_element(2)
  LIST_ONE.print_list(LIST_ONE.head)
  print('Removing element-0 from Linked List=>')
  LIST_ONE.remove_nth_element(0)
  LIST_ONE.print_list(LIST_ONE.head)
    
  print('Copy of a Linked List')
  LIST_TWO = LIST_ONE.copy_list()
  LIST_TWO.print_list(LIST_TWO.head)

  # Building a List with cycle to see f we can detect a cycle.
  LIST_THREE = LIST_ONE.copy_list()
  last_node = LIST_THREE.return_last_node()
  LIST_THREE.print_list(LIST_THREE.head)
  print('Detect a cycle: {}'.format(LIST_THREE.detect_loop()))
  last_node.next = LIST_THREE.head
  print('Detect a cycle: {}'.format(LIST_THREE.detect_loop()))
