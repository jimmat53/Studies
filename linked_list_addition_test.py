import unittest
from linked_list_addition import LinkedList, IntegerLinkedList

class LinkedListAdditionTest(unittest.TestCase):
	def setup(self):
		pass

	def testLength(self):
		ll = LinkedList()
		ll.append('a')
		ll.append('b')
		ll.append('c')
		self.assertEqual(ll.length(),3)

	def testAddition(self):
		x = IntegerLinkedList()
		x.buildNumber([1, 2, 0, 4,  5])
		y = IntegerLinkedList()
		y.buildNumber([1, 2, 0, 4,  5])
		z = x + y
		self.assertEqual(int(z), 24090)

		x = IntegerLinkedList()
		x.buildNumber([5, 5, 5,  5])
		y = IntegerLinkedList()
		y.buildNumber([5, 5, 5,  5])
		z = x + y
		self.assertEqual(int(z), 11110)

		x = IntegerLinkedList()
		x.buildNumber([0, ])
		y = IntegerLinkedList()
		y.buildNumber([0, ])
		z = x + y
		self.assertEqual(int(z), 0)
		
		x = IntegerLinkedList()
		x.buildNumber([1, 5, 4, 6, 7, 8])
		y = IntegerLinkedList()
		y.buildNumber([1, ])
		z = x + y
		self.assertEqual(int(z), 154679)

if __name__ == "__main__":
	unittest.main()
