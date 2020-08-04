'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，
一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
'''


class RandomListNode(object):
	def __init__(self, x):
		self.label=x
		self.next=None # 指向下一个节点的指针
		self.random=None #  每一个节点随意指向的指针，可能为null

class Solution(object):
	# 返回RandomListNode
	def Clone(self, pHead):
		if pHead==None:
			return None
		self.CloneNodes(pHead)
		self.ConnectRandomNodes(pHead)
		return self.ReconnectNodes(pHead)

	# 复制原始链表的每个结点, 将复制的结点链接在其原始结点的后面
	def CloneNodes(self, pHead):
		pNode=pHead
		while pNode:
			pCloned=RandomListNode(0)
			pCloned.label=pNode.label
			pCloned.next=pNode.next
			pNode.next=pCloned
			pNode=pCloned.next

	# 将复制后的链表中的复制结点的random指针链接到被复制结点random指针的后一个结点
	def ConnectRandomNodes(self, pHead):
		pNode=pHead
		while pNode:
			pCloned=pNode.next
			if pNode.random!=None:
				pCloned.random=pNode.random.next 
			pNode=pCloned.next

	# 拆分链表, 将原始链表的结点组成新的链表, 复制结点组成复制后的链表
	def ReconnectNodes(self, pHead):
		pNode=pHead
		pClonedHead=pClonedNode=pNode.next 
		pNode.next=pClonedHead.next
		pNode=pNode.next 

		while pNode:
			
			pClonedNode.next=pNode.next 
			pClonedNode=pClonedNode.next 
			pNode.next=pClonedNode.next 
			pNode=pNode.next 

		return pClonedHead

	def Clone1(self, pHead):
		if pHead==None:
			return None 
		self.CloneNodes1(pHead)
		self.ConnectRandomNodes1(pHead)
		return self.ReconnectNodes1(pHead)

	def CloneNodes1(self, pHead):
		pNode=pHead
		while pNode:
			pCloned=RandomListNode(0)
			pCloned.label=pNode.label
			pCloned.next=pNode.next
			pNode.next=pCloned 
			pNode=pCloned.next 

	def ConnectRandomNodes1(self, pHead):
		pNode=pHead
		while pNode:
			pCloned=pNode.next 
			if pNode.random!=None:
				pCloned.random=pNode.random.next 
			pNode=pCloned.next 

	def ReconnectNodes(self, pHead):
		pNode=pHead
		pClonedHead=pClonedNode=pNode.next 
		pNode.next=pClonedHead.next
		pNode=pNode.next 

		while pNode:
			pClonedNode.next=pNode.next 
			pClonedNode=pClonedNode.next 
			pNode.next=pClonedNode.next 
			pNode=pNode.next 

		return pClonedHead

	def ReconnectNodes(self, pHead):
		pNode=pHead 
		pClonedHead=pClnedNode=pNode.next 
		pNode.next=pClonedHead.next 
		pNode=pNode.next 

		while pNode:
			pClonedNode.next=pNode.next
			pClonedNode=pClonedNode.next 
			pNode.next=pClonedNode.next 
			pNode=pNode.next 

		return pClonedHead


node1 = RandomListNode(1)
node2 = RandomListNode(3)
node3 = RandomListNode(5)
node1.next = node2
node2.next = node3
node1.random = node3

S = Solution()
clonedNode = S.Clone(node1)
print(clonedNode.random.label)







































