# Add 2 positive integers using Linked List

import copy

class EmptyDigits(Exception):
	pass
class InvalidDigit(Exception):
	pass

class Node:
	'''One node in a single linked list'''
	def __init__(self, value):
		''' Create a node for a Linked List'''
		self.value = value
		self.next = None

class LinkedList:
	'''Integer Linked List'''

	def __init__(self):
		self.start_ptr = None
		self.end_ptr = None
	
	def append(self, value):
		new_node = Node(value)
		if self.start_ptr is None:
			self.start_ptr = new_node
		else:
			self.end_ptr.next = new_node	# Append to the current end node
		self.end_ptr = new_node	# Set a new end node
	
	def __str__(self):
		traverse_node = self.start_ptr
		result = ""
		while(traverse_node):
			result = result + str(traverse_node.value) + ", "
			traverse_node = traverse_node.next
		return result[0:-2]
	
	def length(self):
		counter = 0
		traverse_node = self.start_ptr
		while(traverse_node):
			counter += 1
			traverse_node = traverse_node.next
		return counter
	
	def reverse(self):
		traverse_node = self.start_ptr
		while(traverse_node):
			current_node = traverse_node
			tmp = current_node.next
			if current_node == self.start_ptr:
				current_node.next = None
				self.end_ptr = current_node
			else:
				current_node.next = prev
			prev = current_node
			traverse_node = tmp
		self.start_ptr = prev
				

class IntegerLinkedList(LinkedList):
	'''Linked list with each node representing the digits of a number'''

	def validate(self, digits):
		if type(digits) is not list:
			raise InvalidDigit
		if len(digits) == 0:
			raise EmptyDigits
		for digit in digits:
			if type(digit) is not int:
				raise InvalidDigit
		return True
	
	def reverse(self):
		return super().reverse()

	def buildNumber(self, digits):
		'''Build an integer linked list using a digits array.'''
		try:
			self.validate(digits)
		except (EmptyDigits, InvalidDigit):
			print("Invalid or empty digits.")
		for digit in digits:
			self.append(digit)
	
	def __add__(self, second):
		''' Add 2 integer linked lists. '''
		x = copy.deepcopy(self)
		y = copy.deepcopy(second)
		x.reverse()
		y.reverse()
		if x.length() > y.length():
			traverse_node1 = x.start_ptr
			traverse_node2 = y.start_ptr
		else:
			traverse_node1 = y.start_ptr
			traverse_node2 = x.start_ptr
		
		result = []
		carry = 0
		while(traverse_node1):
			digit1 = traverse_node1.value
			traverse_node1 = traverse_node1.next
			if traverse_node2:
				digit2 = traverse_node2.value
				traverse_node2 = traverse_node2.next
			else:
				digit2 = 0
			sum_digits = digit1 + digit2 + carry
			if sum_digits >= 10:
				carry = int(sum_digits / 10)
				sum_digits = sum_digits % 10
			else:
				carry = 0
			result.append(sum_digits)
			
		if carry:
			result.append(carry)
		result_ll = IntegerLinkedList()
		result_ll.buildNumber(result)
		result_ll.reverse()
		return result_ll

	def __str__(self):
		return super().__str__()

	def length(self):
		return super().length()
		
		
	
if __name__ == "__main__":
	int1 = IntegerLinkedList()
	int1.buildNumber([1, 2, 0, 4,  5])

	int2 = IntegerLinkedList()
	int2.buildNumber([1, 3, 5])

	print(int1)
	print(int2)
	
	int3 = int1 + int2
	print(int1)
	print(int2)
	print("Sum: " + str(int3))

