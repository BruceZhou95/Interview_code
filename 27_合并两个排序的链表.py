
'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

class ListNode(object):

	def __init__(self, x):
		self.data=x
		self.next=None

class Solution(object):

	def Merge(self, pHead1, pHead2):
		if pHead1==None and pHead2==None:
			return None
		elif pHead1==None:
			return pHead2
		elif pHead2==None:
			return pHead1

		pMergedHead=None
		if pHead1.data<pHead2.data:
			pMergedHead=pHead1
			pMergedHead.next=self.Merge(pHead1.next, pHead2)
		else:
			pMergedHead=pHead2
			pMergedHead.next=self.Merge(pHead1, pHead2.next)

		return pMergedHead




	def Merge1(self, pHead1, pHead2):

		if pHead1==None and pHead2==None:
			return None
		elif pHead2==None:
			return pHead1
		elif pHead1==None:
			return pHead2

		pMergedHead=None
		if pHead1.data<pHead2.data:
			pMergedHead=pHead1
			pMergedHead.next=self.Merge1(pHead1.next, pHead2)

		else:
			pMergedHead=pHead2
			pMergedHead.next=self.Merge1(pHead1, pHead2.next)

		return pMergedHead




	def Merge2(self, pHead1, pHead2):

		if pHead2==None and pHead1==None:
			return None
		elif pHead2==None:
			return pHead1
		elif pHead1==None:
			return pHead2

		pMergedHead=None # 新的链表的头结点
		if pHead1.data<pHead2.data:
			pMergedHead=pHead1
			pMergedHead.next=self.Merge2(pHead1.next, pHead2)

		else:
			pMergedHead=pHead2
			pMergedHead.next=self.Merge2(pHead1, pHead2.next)

		return pMergedHead




node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)
node1.next = node2
node2.next = node3

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)
node4.next = node5
node5.next = node6

S = Solution()
S.Merge(node1, node4)
print(node4.next.data)





































