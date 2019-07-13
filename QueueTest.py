"""Tests for Queue class."""

import unittest
from queue import Queue, EmptyQueue

class QueueTest(unittest.TestCase):
	
  def setup(self):
    pass
	
  def testIsEmpty(self):
    q = Queue()
    self.assertTrue(q.isEmpty())
    q.enqueue(1)
    self.assertFalse(q.isEmpty())

  def testEnqueue(self):
    q = Queue()
    q.enqueue(100)
    self.assertEqual(len(q.queue), 1)
    q.enqueue(200)
    q.enqueue(300)
    self.assertItemsEqual(q.queue, [100, 200, 300])
    q.enqueue(400)
    self.assertEqual(len(q.queue), 3)
    self.assertItemsEqual(q.queue, [200, 300, 400])

  def testDequeue(self):
    q = Queue()
    with self.assertRaises(EmptyQueue):
      q.dequeue()
    q.enqueue(100)
    x = q.dequeue()
    self.assertEqual(x, 100)

if __name__ == "__main__":
	unittest.main()
