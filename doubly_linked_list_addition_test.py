import unittest
from doubly_linked_list_addition import IntegerLinkedList

class IntegerLinkedListTest(unittest.TestCase):
	def setup(self):
		pass
		
	def testBuildNumber(self):
		x = IntegerLinkedList()
		x.BuildNumber([1, 2, 3])
		self.assertEqual(str(x), '123')

	def testBuildAddition(self):
		x = IntegerLinkedList()
		y = IntegerLinkedList()

		x.BuildNumber([1, 2, 3])
		y.BuildNumber([2, 5, 5])
		self.assertEqual(int(x + y), 378)

		x.BuildNumber([1, 7, 5])
		y.BuildNumber([2, 5, 5])
		self.assertEqual(int(x + y), 430)

if __name__ == "__main__":
	unittest.main()
