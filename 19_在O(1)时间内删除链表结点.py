
'''
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
'''

class ListNode(object):

	def __init__(self, x=None):
		self.data=x
		self.next=None 

	def __del__(self):
		self.data=None
		self.next=None

class Solution(object):

	def DeleteNode(self, pListHead, pToBeDeleted):
		r"""
			Args:
				pListHead:链表的头结点
				pToBeDeleted:待删除的节点
		"""
		if not pListHead or not pToBeDeleted:
			return None 

		if pToBeDeleted.next!= None: # 多个节点，删除的是中间结点
			pNext=pToBeDeleted.next 
			pToBeDeleted.data=pNext.data
			pToBeDeleted.next=pNext.next
			pNext.__del__()

		elif pListHead==pToBeDeleted: # 唯一的一个节点，要删除
			pToBeDeleted.__del__()
			pListHead.__del__()

		else: # 删除的是尾结点
			pNode=pListHead
			while pNode.next!=pToBeDeleted:
				pNode=pNode.next 
			pNode.next=None 
			pToBeDeleted.__del__()

	def DeletedNode1(self, pListHead, pToBeDeleted):

		if not pListHead and not pToBeDeleted:
			return 

		if pToBeDeleted.next!=None:
			pNext=pToBeDeleted.next
			pToBeDeleted.next=pNext.next
			pToBeDeleted.data=pNext.data
			pNext.__del__()

		elif pToBeDeleted==pListHead:
			pToBeDeleted.__del__()
			pListHead.__del__()

		else:
			pNode=pListHead
			while pNode.next!=pToBeDeleted:
				pNode=pNode.next
			pNode=None 
			pToBeDeleted.__del__()

	def DeletedNode2(self, pListHead, pToBeDeleted):

		if not pListHead and not pToBeDeleted:
			return 

		if pToBeDeleted.next!=None:
			pNext=pToBeDeleted.next
			pToBeDeleted.next=pNext.next
			pToBeDeleted.data=pNext.data
			pNext.__del__()

		elif pListHead==pToBeDeleted:
			pListHead.__del__()
			pToBeDeleted.__del__()

		else:
			pNode=pListHead 
			while pNode.next!=pToBeDeleted:
				pNode=pNode.next
			pNode=None 
			pToBeDeleted.__del__()

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4

S = Solution()
S.DeletedNode2(node1, node3)
print(node3.data)
S.DeletedNode2(node1, node3)
print(node3.data)
print(node2.data)
S.DeletedNode2(node1, node1)
print(node1.data)
S.DeletedNode2(node1, node1)
print(node1.data)












































