import unittest
from dequeue import DeQueue, EmptyDeQueue

class DequeueTest(unittest.TestCase):
	def setup(self):
		pass
	
	def testIsEmpty(self):
		dq = DeQueue()
		self.assertTrue(dq.isEmpty())

	def testInsertFront(self):
		dq = DeQueue()
		dq.insertFront(1)
		dq.insertFront(2)
		dq.insertFront(3)
		self.assertEqual(dq.dequeue, [3, 2, 1])
		dq.insertFront(4)
		self.assertEqual(dq.dequeue, [4, 3, 2])
		dq.insertFront(5)
		self.assertEqual(dq.dequeue, [5, 4, 3])

	def testInsertLast(self):
		dq = DeQueue()
		dq.insertLast(1)
		dq.insertLast(2)
		dq.insertLast(3)
		self.assertEqual(dq.dequeue, [1, 2, 3])
		dq.insertLast(4)
		self.assertEqual(dq.dequeue, [2, 3, 4])
		dq.insertLast(5)
		self.assertEqual(dq.dequeue, [3, 4, 5])

	def testDeleteFront(self):
		dq = DeQueue()
		with self.assertRaises(EmptyDeQueue):
			dq.deleteFront()
		dq.insertLast(1)
		dq.insertLast(2)
		dq.insertLast(3)
		dq.deleteFront()
		self.assertEqual(dq.dequeue, [2, 3])
		dq.insertFront(1)
		self.assertEqual(dq.dequeue, [1, 2, 3])
		dq.insertLast(4)
		self.assertEqual(dq.dequeue, [2, 3, 4])
		dq.deleteFront()
		self.assertEqual(dq.dequeue, [3, 4])

	def testDeleteLast(self):
		dq = DeQueue()
		with self.assertRaises(EmptyDeQueue):
			dq.deleteLast()
		dq.insertLast(1)
		dq.insertLast(2)
		dq.insertLast(3)
		dq.deleteLast()
		self.assertEqual(dq.dequeue, [1, 2])
		dq.insertLast(3)
		self.assertEqual(dq.dequeue, [1, 2, 3])
		dq.insertLast(4)
		self.assertEqual(dq.dequeue, [2, 3, 4])
		dq.deleteLast()
		self.assertEqual(dq.dequeue, [2, 3])
		dq.insertFront(1)
		dq.insertFront(0)
		self.assertEqual(dq.dequeue, [0, 1, 2])
		dq.deleteLast()
		self.assertEqual(dq.dequeue, [0, 1])

if __name__ == '__main__':
	unittest.main()
