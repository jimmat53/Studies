import unittest
from stack import Stack, EmptyStack

class StackTest(unittest.TestCase):
  def testPush(self):
    s = Stack()
    s.push(100)
    self.assertEqual(len(s.stack), 1)
    self.assertEqual(s.stack[0], 100)

  def testPop(self):
    s = Stack()
    with self.assertRaises(EmptyStack):
      s.pop()
    s.push(100)
    x = s.pop()
    self.assertEqual(x, 100)
    


if __name__ == "__main__":
  unittest.main()
