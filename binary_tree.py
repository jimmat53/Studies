class Node:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

class Tree:
	traverse_result = []
	def __init__(self):
		self.rootnode = self.BuildTree()
		
	def BuildTree(self):
		'''Builds an example tree and returns the root node. 
		
							1
					2				3
				4		5		6		7
		'''
		rootnode = Node(1, None, None)
		leftnode = Node(2, None, None)
		rightnode = Node(3, None, None)
		rootnode.left = leftnode
		rootnode.right = rightnode
		leftnode.left = Node(4, None, None)
		leftnode.right = Node(5, None, None)
		rightnode.left = Node(6, None, None)
		rightnode.right = Node(7, None, None)
		return rootnode

	def PreOrderTraversal(self, current_node, result):
		result.append(current_node.value)
		if current_node.left:
			self.PreOrderTraversal(current_node.left, result)
		if current_node.right:
			self.PreOrderTraversal(current_node.right, result)
		return result

	def InOrderTraversal(self, current_node):
		if current_node.left:
			self.InOrderTraversal(current_node.left)
		Tree.traverse_result.append(current_node.value)
		if current_node.right:
			self.InOrderTraversal(current_node.right)			
		return Tree.traverse_result

	def PostOrderTraversal(self, current_node):
		if current_node.left:
			self.PostOrderTraversal(current_node.left)
		if current_node.right:
			self.PostOrderTraversal(current_node.right)	
		Tree.traverse_result.append(current_node.value)
		return Tree.traverse_result

if __name__ =="__main__":
	tree1 = Tree()
	Tree.traverse_result = []
	tree1.PreOrderTraversal(tree1.rootnode, [])
	print(Tree.traverse_result)
	
