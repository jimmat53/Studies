'''Perform addition of 2 integers represented as doubly linked lists'''

class EmptyDigits(Exception):
	pass

class InvalidDigit(Exception):
	pass

class Node:
	def __init__(self, value, next=None, prev=None):
		self.value = value
		self.next = next
		self.prev = prev


class DoublyLinkedList:
	def __init__(self):
		self.start_ptr = None
		self.end_ptr = None

	def append(self, value):
		new_node = Node(value)
		if self.start_ptr is None:
			self.start_ptr = new_node
		else:
			new_node.prev = self.end_ptr
			self.end_ptr.next = new_node
		self.end_ptr = new_node
	
	def __str__(self):
		traverse_node = self.start_ptr
		elems = []
		while(traverse_node):
			elems.append(traverse_node.value)
			traverse_node = traverse_node.next
		return ", ".join(list(map(lambda x: str(x), elems)))
	
	def __len__(self):
		traverse_node = self.start_ptr
		counter = 0
		while(traverse_node):
			counter += 1
			traverse_node = traverse_node.next
		return counter

class IntegerLinkedList(DoublyLinkedList):
	def BuildNumber(self, digits=[]):
		if type(digits) is not list:
			raise InvalidDigit
		if len(digits) == 0:
			raise EmptyDigits
		for digit in digits:
			if type(digit) is not int:
				raise InvalidDigit

		# Create a new number
		self.start_ptr = None
		self.end_ptr = None
		
		for digit in digits:
			self.append(digit)
	
	def __repr__(self):
		return(__str__())

	def __str__(self):
		traverse_node = self.start_ptr
		elems = []
		while(traverse_node):
			elems.append(traverse_node.value)
			traverse_node = traverse_node.next
		return "".join(list(map(lambda x: str(x), elems)))
		
	def __int__(self):
		traverse_node = self.start_ptr
		result = 0
		while(traverse_node):
			result = result * 10 + traverse_node.value
			traverse_node = traverse_node.next
		return result

	def __add__(self, second):
		if len(self) > len(second):
			traverse_node = self.end_ptr
			other_node = second.end_ptr
		else:
			traverse_node = second.end_ptr
			other_node = self.end_ptr

		carry = 0
		result = []
		while(traverse_node):
			digit1 = traverse_node.value
			digit2 = other_node.value
			sum_digits = digit1 + digit2 + carry
			carry = int(sum_digits/10)
			result.append(sum_digits%10)
			traverse_node = traverse_node.prev
			other_node = other_node.prev
		if carry:
			result.append(carry)
		result.reverse()
		result_ll = IntegerLinkedList()
		result_ll.BuildNumber(result)
		return result_ll
			
if __name__ =="__main__":
	num1 = IntegerLinkedList()
	num2 = IntegerLinkedList()
	try:
		num1.BuildNumber([1, 2, 3])
		num2.BuildNumber([1, 2, 3])
	except (InvalidDigit, EmptyDigits) as e:
		print("Enter a valid number")
	num3 = num1 + num2
	print(num3)
	
