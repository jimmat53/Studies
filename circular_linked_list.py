"""Circular LinkedList."""

class LinkedListException(Exception):
  pass


class Node:
  """A node of a circular linked list."""

  def __init__(self, data):
    """Node constructor."""
    self.data = data
    self.next = None

  def __repr__(self):
    return 'Data: {}, Next(ObjID): {}'.format(str(self.data), str(id(self.next)))


class CircularLinkedList():
  """LinkedList data structure and operations on it."""

  def __init__(self):
    self.head = None

  def append(self, value):
    """Append a node to a LinkedList."""
    new_node = Node(value)
    if self.head:
      node = self.head
      while node.next != self.head:
        node = node.next
      node.next = new_node
    else:
      self.head = new_node
    new_node.next = self.head

  def print_list(self):
    """Print the LinkedList."""
    node = self.head
    if self.head:
      while True:
	print str(node.data)
	node = node.next
	if node == self.head:
	  break
    else:
      print '<Empty List>'

  def reverse_list(self):
    """Reverse the LinkedList object."""
    if self.head:
      prev = self.head
      current = self.head.next
      while current != self.head:
	tmp = current.next
	current.next = prev
	prev = current
	current = tmp
      self.head.next = prev
      self.head = prev

  def delete(self, ele):
    """Delete an element in the Linkedlist."""
    prev = current = self.head
    element_in_head = False
    if self.head:
      while True:
	if current.data == ele:
	  if current == self.head:
	    element_in_head = True
	  else:
	    prev.next = current.next
	    break
	prev = current
	current = current.next
	if current == self.head:
	  break
      if element_in_head:
	if self.head.next == self.head:
	  self.head = None
	else:
	  prev.next = self.head.next
	  self.head = self.head.next

  def search(self, ele):
    """Search for an element in the Linkedlist."""
    if self.head:
      current = self.head
      while True:
	if current.data == ele:
	  return True
	current = current.next
	if current == self.head:
	  break
    return False

  def insert_middle(self, ele, position):
    """Insert an element at the nth position in the Linkedlist."""
    if position == 0 and not self.head:
      new_node = Node(ele)
      new_node.next = new_node
      self.head = new_node
    elif position > self.length():
      raise LinkedListException
    else:
      current = self.head
      prev = self.head
      counter = 0
      while counter < position:
        counter = counter + 1
        prev = current
        current = current.next
      new_node = Node(ele)
      new_node.next = current
      if counter == 0:
        self.head = new_node
      prev.next = new_node

  def remove_nth_element(self, position):
    """Remove an element at the nth position in the Linkedlist."""
    if not self.head or position > self.length() -1:
      raise LinkedListException
    if position == 0 and self.head == self.head.next:
      self.head = None
    else:
      current = self.head
      prev = self.head
      counter = 0
      while counter < position or position == 0:
        counter += 1
        prev = current
        current = current.next
	if current == self.head:
	  break
      if position == 0:
        self.head = current.next
      prev.next = current.next

  def length(self):
    """Find the length of the Linkedlist."""
    if self.head:
      count = 1
      current = self.head
      while(current.next != self.head):
	count+=1
	current = current.next
      return count
    else:
      return 0
    
  def return_last_node(self):
    """Return the last node of the list."""
    if self.head:
      current = self.head
      while True:
	prev = current
	current = current.next
	if current == self.head:
	  break
      return prev
    else:
      return None

  def copy_list(self):
    """Return a copy of the Linkedlist object ."""
    if self.head:
      LIST_COPY = CircularLinkedList()
      current = self.head
      while True:
	LIST_COPY.append(current.data)
	current = current.next
	if current == self.head:
	  break
      return LIST_COPY
    else:
      return CircularLinkedList()

  def detect_loop(self):
    """Detect cycles in Linkedlist."""
    tortoise = self.head
    hare = self.head
    while hare:
      tortoise = tortoise.next
      hare = hare.next.next
      if tortoise == hare:
        return True
    return False


if __name__ == "__main__":
  LIST_ONE = CircularLinkedList()
  LIST_ONE.append(1)
  LIST_ONE.append(2)
  LIST_ONE.append(3)
  LIST_ONE.append(4)
  print('Linked List=>')
  LIST_ONE.print_list()

  LIST_ONE.reverse_list()
  print('Reversed Linked List=>')
  LIST_ONE.print_list()
    
  print('Delete an element from Linked List=>')
  LIST_ONE.delete(3)
  LIST_ONE.delete(1)
  LIST_ONE.delete(2)
  LIST_ONE.delete(4)
  LIST_ONE.print_list()

  print('Length of the Linked List=>')
  print(LIST_ONE.length())

  print('If element is present=>')
  LIST_ONE.append(1)
  LIST_ONE.append(2)
  LIST_ONE.append(3)
  LIST_ONE.append(4)
  print(LIST_ONE.search(2))
  print(LIST_ONE.search(100))
  
  print('Insert in the middle of the Linked List=>')
  LIST_ONE = CircularLinkedList()
  LIST_ONE.insert_middle(0, 0)
  LIST_ONE.insert_middle(1, 1)
  LIST_ONE.insert_middle(3, 2)
  LIST_ONE.insert_middle(2, 2)
  LIST_ONE.insert_middle(2, 4)
  print('Linked List=>')
  LIST_ONE.print_list()

  try:
    LIST_ONE.insert_middle(100, 100)
  except LinkedListException:
    print('Invalid position')

  print('Removing element-4 from Linked List=>')
  LIST_ONE.remove_nth_element(4)
  LIST_ONE.print_list()
  print('Removing element-2 from Linked List=>')
  LIST_ONE.remove_nth_element(2)
  LIST_ONE.print_list()
  print('Removing element-0 from Linked List=>')
  LIST_ONE.remove_nth_element(0)
  LIST_ONE.print_list()

  print('Last node of a Linked List=>')
  last = LIST_ONE.return_last_node()
  print last
  
  print('Copy of a Linked List')
  LIST_TWO = LIST_ONE.copy_list()
  LIST_TWO.print_list()

  print('Detect a cycle: {}'.format(LIST_TWO.detect_loop()))
