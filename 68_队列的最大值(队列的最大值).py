
'''
请定义一个队列并实现函数max得到队列里的最大值，要求函数max、push_back和pop_front 的时间复杂度都是0(1)。
'''
import queue 
class MaxQueue:

	def __init__(self):
		self.deque = queue.deque()

	def max_value(self):
		return  max(self.deque) if self.deque else -1

	def push_back(self, value):
		self.deque.append(value)


	def pop_front(self):
		return self.deque.popleft() if self.deque else -1

class MaxQueue1(object):
	def __init__(self):
		self.deque=queue.deque()

	def max_value(self):
		return max(self.deque) if self.deque else -1

	def push_back(self, value):

		self.deque.append(value)

	def pop_front(self):
		return self.deque.popleft() if self.deque else -1

	
















































