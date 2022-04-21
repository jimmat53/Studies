import unittest
from binary_tree import Tree

class TreeTest(unittest.TestCase):
	def setUp(self):
		self.test_tree = Tree()
		self.root_node = self.test_tree.BuildTree()

	def testPreOrderTraversal(self):
		result = self.test_tree.PreOrderTraversal(self.root_node, [])
		self.assertEqual(result, [1, 2, 4, 5, 3, 6, 7])

	def testInOrderTraversal(self):
		Tree.traverse_result = []
		result = self.test_tree.InOrderTraversal(self.root_node)
		self.assertEqual(result, [4, 2, 5, 1, 6, 3, 7])

	def testPostOrderTraversal(self):
		Tree.traverse_result = []
		result = self.test_tree.PostOrderTraversal(self.root_node)
		self.assertEqual(result, [4, 5, 2, 6, 7, 3, 1])

if __name__ == "__main__":
	unittest.main()
