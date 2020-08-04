


"""
	用两个栈来实现一个队列，来完成push和pop操作，队列中的元素为int类型
"""

class Solution(object):

	def __init__(self):
		self.stack1=[]
		self.stack2=[]

	def push(self, node):
		self.stack1.append(node)

	def pop(self):
		if len(self.stack1)==0 and len(self.stack2)==0:
			return 

		elif len(self.stack2)==0:
			while len(self.stack1)>0:
				self.stack2.append(self.stack1.pop())
		return self.stack2.pop()


p=Solution()

p.push(10)
p.push(11)
p.push(12)
print(p.pop())


class Solution2(object):

	def __init__(self):
		self.stack1=[]
		self.stack2=[]

	def push(self, node):
		self.stack1.append(node)

	def pop(self):
		if len(self.stack1)==0 and len(self.stack2)==0:
			return 
		elif len(self.stack2==0):
			while self.stack1>0:
				self.stack2.append(self.stack1.pop())
		return self.stack2.pop()



class Solution3(object):

	def __init__(self):
		self.stack1=[]
		self.stack2=[]

	def push(self, node):
		self.stack1.append(node)

	def pop(self):
		if len(self.stack1==0) and len(self.stack2==0):
			return 

		if (len(self.stack2)==0):
			while len(self.stack1)>0:
				self.stack2.append(self.stack1.pop())

		return self.stack2.pop()




































