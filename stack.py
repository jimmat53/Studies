"""Simple Stack."""

class EmptyStack(Exception):
	"""Exception to throw for empty stack."""

class Stack:
	def __init__(self):
		self.stack = []
	
	def push(self, ele):
		self.stack.append(ele)
	
	def pop(self):
		try:
			ele = self.stack.pop()
		except IndexError:
			raise EmptyStack
		return ele

if __name__ == "__main__":
	one = Stack()
	one.push(1)
	one.push(2)
	print(one.pop())
	print(one.pop())
	try:
		print(one.pop())
	except EmptyStack:
		print("Pop failed, as stack is empty.")
