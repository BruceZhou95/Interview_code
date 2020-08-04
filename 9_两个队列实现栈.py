
"""
	使用两个队列实现栈
"""

class Solution(object):

	def __init__(self):
		self.queue1=[]
		self.queue2=[]

	def push(self, x):
		if self.queue2==[]:
			self.queue1.append(x)
		else:
			self.queue2.append(x)

	def pop(self):
		if not self.queue1 and not self.queue2:
			return 
		if self.queue1!=[]:
			length=len(self.queue1)
			for i in range(length-1):
				self.queue2.append(self.queue1.pop(0))
			return self.queue1.pop()

		else:
			length=len(self.queue2)
			for i in range(length-1):
				self.queue1.append(self.queue2.pop(0))
			return self.queue2.pop()


class Solution2(object):

	def __init__(self):
		self.queue1=[]
		self.queue2=[]

	def push(self, x):
		if self.queue2==[]:
			self.queue1.append(x)
		else:
			self.queue2.append(x)

	def pop(self):
		if not self.queue2 and not self.queue1:
			return 

		if self.queue1!=[]:
			length=len(self.queue1)
			for i in range(length-1):
				self.queue2.append(self.queue1.pop(0))
			return self.queue1.pop()

		else:
			length=len(self.queue2)
			for i in range(length-1):
				self.queue1.append(self.queue2.pop(0))
			return self.queue2.pop()

class Solution3(object):

	def __init__(self):
		self.queue1=[]
		self.queue2=[]

	def push(self, data):
		if self.queue2==[]:
			self.queue1.append(data)
		else:
			self.queue2.append(data)

	def pop(self):
		if not self.queue1 and not self.queue2:
			return 

		if self.queue1!=[]:
			length=len(self.queue1)
			for i in range(length-1):
				self.queue2.append(self.queue1.pop(0))
			return self.queue1.pop()
		else:
			length=len(self.queue2)
			for i in range(length-1):
				self.queue1.append(self.queue2.pop(0))
			return self.queue2.pop()

class Solution4(object):

	def __init__(self):
		self.queue1=[]
		self.queue2=[]

	def push(self, data):
		if self.queue2==[]:
			self.queue1.append(data)
		else:
			self.queue2.append(data)

	def pop(self):
		if not self.queue1 and not self.queue2:
			return 

		if self.queue1!=[]:
			length=len(self.queue1)
			for i in range(length-1):
				self.queue2.append(self.queue1.pop(0))
			return self.queue1.pop()

		else:
			length=len(self.queue2)
			for i in range(length-1):
				self.queue1.append(self.queue2.pop(0))
			return self.queue2.pop()


class Solution2(object):

	def __init__(self):
		self.queue1=[]
		self.queue2=[]

	def push(self, data):

		if self.queue2==[]:
			self.queue1.append(data)
		else:
			self.queue2.append(data)

	def pop(self):
		if self.queue1==[] and self.queue2==[]:
			return 

		if self.queue1!=[]:
			length=len(self.queue1)
			for i in range(length-1):
				self.queue2.append(self.queue1.pop(0))
			return self.queue1.pop()

		else:
			length=len(self.queue2)
			for i in range(length-1):
				self.queue1.append(self.queue2.pop(0))
			return self.queue2.pop()


































