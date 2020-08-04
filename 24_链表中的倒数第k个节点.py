'''
输入一个链表，输出该链表中倒数第k个结点。
'''

'''
这道题的思路很好
如果在只希望一次遍历的情况下, 寻找倒数第k个结点, 可以设置两个指针
第一个指针先往前走k-1步, 然后从第k步开始第二个指针指向头结点
然后两个指针一起遍历
当地一个指针指向尾节点的时候, 第二个指针正好指向倒数第k个结点
推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,  快指针指到尾部, 慢指针正好指到中间
'''

class ListNode(object):

	def __init__(self, x):
		self.data=x
		self.next=None

class Solution(object):

	def FindKthToTail(self, head, k):
		if head==None or k<=0:
			return None 

		pAhead=head 
		pBehind=None 

		for i in range(k-1):
			if pAhead.next!=None:
				pAhead=pAhead.next 
			else:
				return None 
		pBehind=head
		while pAhead.next!=None:
			pAhead=pAhead.next
			pBehind=pBehind.next 
		return pBehind

	def FindKthToTail(self, head, k):

		if head==None or k<=0:
			return None 

		pAhead=head
		pBehind=head

		for i in range(k-1):
			if pAhead.next!=None:
				pAhead=pAhead.next 
			else:
				return None 

		while (pAhead.next!=None):
			pAhead=pAhead.next 
			pBehind=pBehind.next

		retrun pBehind


	# 找到中间结点
	def FindMiddle(self, head):

		if head==None:
			return None 
		if head.next==None:
			return head

		pAhead=head
		pBehind=head

		while pAhead.next!=None:
			pBehind=pBehind.next
			pAhead=pAhead.next 
			if pAhead:
				pAhead=pAhead.next
			 

		return pBehind








































