

class Stack:
	def __init__(self):
		self.top = -1
		self.data = []

	def get_top(self):
		return self.data[self.top]

	def empty(self):
		return not len(self.data)

	def push(self, x: object) -> object:
		self.top += 1
		return self.data.append(x)

	def pop(self):
		if self.empty():
			return False
		else:
			self.top -= 1
			return self.data.pop()


def main():
	stack = Stack()

	stack.push(1)
	stack.push(3)
	stack.push(5)
	assert(stack.pop() == 5)

	stack.push(7)
	stack.push(11)

	assert(stack.get_top() == 11)
	assert(stack.pop() == 11)
	assert(stack.pop() == 7)
	assert(stack.get_top() == 3)
	assert(stack.pop() == 3)
	assert(stack.pop() == 1)
	assert(stack.pop() is False and stack.top == -1 and stack.empty())

main()
