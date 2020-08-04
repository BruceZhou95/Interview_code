'''
输入两个链表，找出它们的第一个公共节点。
'''

class ListNode(object):

	def __init__(self, x):
		self.val=x
		self.next=None

class Solution(object):

	def FindFirstCommonNode(self, pHead1, pHead2):
		len1 = self.getChainLen(pHead1)
		len2 = self.getChainLen(pHead2)
		print(len1, len2)
		diff=0
		if len2 > len1:
			pHead1, pHead2 = pHead2, pHead1
			diff = abs(len1-len2)
			while diff > 0:
				pHead1 = pHead1.next
				diff -= 1
		print()
		while pHead1 != pHead2:
			pHead1 = pHead1.next
			pHead2 = pHead2.next
		return pHead1

	def getChainLen(self, Head):
		chainLen = 0
		while Head:
			chainLen += 1
			Head = Head.next
		return chainLen

	def FindFirstCommonNode1(self, pHead1, pHead2):
		p1, p2 = pHead1, pHead2
		while p1 != p2:
			p1 = p1.next if p1 != None else pHead2
			p2 = p2.next if p2 != None else pHead1
			
		return p1


node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)
node6=ListNode(6)
node7=ListNode(7)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7

node41=ListNode(4)
node51=ListNode(5)
node61=ListNode(6)
node71=ListNode(7)
node41.next=node51
node51.next=node61
node61.next=node71

s=Solution()
# print(s.FindFirstCommonNode(node1, node41))
print(s.FindFirstCommonNode1(node1, node41))






















































