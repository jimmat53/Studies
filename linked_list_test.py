import unittest
from linked_list import Node
from linked_list import LinkedList
from linked_list import LinkedListException

class LinkedListTest(unittest.TestCase):
  def testNode(self):
    one = Node(1)
    self.assertEqual(one.data, 1)
    self.assertIsNone(one.next)

  def testInitLinkedList(self):
    ll = LinkedList()
    self.assertIsNone(ll.head)

  def testAppend(self):
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    self.assertEqual(ll.head.data, 1)
    self.assertIsNotNone(ll.head.next)
    self.assertEqual(ll.head.next.data, 2)
    self.assertIsNone(ll.head.next.next)

  def testReverseList(self):
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.reverse_list()
    self.assertEqual(ll.head.data, 2)
    self.assertIsNotNone(ll.head.next)
    self.assertEqual(ll.head.next.data, 1)
    self.assertIsNone(ll.head.next.next)

  def testDelete(self):
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.delete(2)
    self.assertEqual(ll.head.data, 1)
    self.assertIsNone(ll.head.next)
    ll.delete(1)
    self.assertIsNone(ll.head)

  def testSearch(self):
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    self.assertTrue(ll.search(1))
    self.assertFalse(ll.search(100))

  def testInsertMiddle(self):
    ll = LinkedList()
    ll.insert_middle(0, 0)
    self.assertEqual(ll.head.data, 0)
    ll.insert_middle(1, 1)
    self.assertEqual(ll.head.next.data, 1)
    ele = 100
    pos = 0
    ll.insert_middle(100, pos)
    self.assertEqual(ll.head.data, 100)

    pos = 1
    ll.insert_middle(200, pos)
    self.assertEqual(ll.head.data, 100)
    self.assertEqual(ll.head.next.data, 200)

  def testRemoveNthElement(self):
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    self.assertEqual(ll.head.data, 1)
    ll.remove_nth_element(0)
    self.assertEqual(ll.head.data, 2)
    ll.remove_nth_element(1)
    self.assertEqual(ll.head.data, 2)
    self.assertIsNone(ll.head.next)

  def testLength(self):
    ll = LinkedList()
    self.assertEqual(ll.length(), 0)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    self.assertEqual(ll.length(), 3)
    
  def testReturnLastNode(self):
    ll = LinkedList()
    self.assertEqual(ll.return_last_node(), None)
    ll.append(1)
    self.assertEqual(ll.return_last_node().data, 1)
    ll.append(2)
    self.assertEqual(ll.return_last_node().data, 2)
    
  def testCopyList(self):
    ll1 = LinkedList()
    ll2 = ll1.copy_list()
    self.assertIsNone(ll2.head)
    ll1.append(1)
    ll1.append(2)
    ll2 = ll1.copy_list()
    self.assertNotEqual(ll1.head, ll2.head) # Make sure, it's a deep copy
    self.assertEqual(ll1.head.data, ll2.head.data)
    self.assertEqual(ll1.head.next.data, ll2.head.next.data)
    self.assertIsNone(ll2.head.next.next)

  def testDetectLoop(self):
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    self.assertFalse(ll.detect_loop())

    element_3 = ll.head.next.next
    self.assertEqual(element_3.data, 3)
    element_3.next = ll.head  # Introducing a loop
    self.assertTrue(ll.detect_loop())
    element_3.next = None
    self.assertFalse(ll.detect_loop())
    
    ll.head.next = ll.head
    self.assertTrue(ll.detect_loop())
    
if __name__ == "__main__":
  unittest.main()
