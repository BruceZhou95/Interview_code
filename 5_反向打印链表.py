
# 反向打印链表

# 定义链表
class ListNode(object):
	def __init__(self, x=None):
		self.data=x
		self.next=None

class Solution(object):

	def printListFromTailToHead(self, listNode):
		if listNode.data==None:
			return 

		L=[]
		head=listNode

		while head:
			L.insert(0, head.data)
			head=head.next 
		return L


class ListNode1(object):

	def __init__(self, data=None):
		self.data=data
		self.next=None 

class Solutio1n(object):

	def printListFromTailTostart1(self, ListNode):
		if listNode.data==None:
			reture 

		L=[]
		head=listNode
		while head:
			L.insert(0, head.data)
			head=head.next 
		return L

node1=ListNode1(3)
node2=ListNode1(5)
node3=ListNode1(12)

node1.next=node2
node2.next=node3

testEmpty=ListNode1()

SingleNode=ListNode1(4) 

class listNode2(onject):

	def __init__(self, data):
		self.data=data 
		self.next=None 

class Solution(object):

	def printlistFromTailTostart2(self, listNode):

		if(listNode.data==None):
			return 
		L=[]

		head=listNode2()
		while head:
			L.insert(0, head.data)
			head=head.next 

		return L


class listNode3(object):

	def __init__(self, data):
		self.data=data 
		self.next=None

class Solution3(object):

	def printlistFromTailTostart3(self, listNode):
		if listNode.data==None:
			return 

		L=[]
		head=listNode3
		while head:
			L.insert(0, head.data)
			head=head.next

		return L 










node1=ListNode(10)
node2=ListNode(11)
node3=ListNode(13)

node1.next=node2
node2.next=node3

singleNode=ListNode(12)
test=ListNode()

S=Solution()

print(S.printListFromTailToHead(node1))
print(S.printListFromTailToHead(test))
print(S.printListFromTailToHead(singleNode))


































