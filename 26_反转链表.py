
'''
反转链表
输入一个链表，反转链表后，输出链表的所有元素
'''

class ListNode(object):
	def __init__(self, x):
		self.data=x
		self.next=None 

class Solution(object):

	# 返回ListNode
	def ReverseList(self, pHead):
		pReversedHead=None
		pNode=pHead
		pPrev=None

		while pNode!=None:
			pNext=pNode.next 

			if pNext==None:
				pReversedHead=pNode

			pNode.next=pPrev
			pPrev=pNode
			pNode=pNext
		return pReversedHead

	def ReverseListRec(self, pHead):
		if not pHead or not pHead.next:
			return pHead
		else:
			pReversedHead=self.ReverseList(pHead.next)
			pHead.next.next=pHead
			pHead.next=None
			return pReversedHead

	def ReverseList1(self, pHead):
		if pHead is None:
			return pHead
		last=None # 指向上一个节点
		while pHead:
			# 先用tmp保存pHead的下一个节点的信息，
			# 保证单链表不会因为失去pHead节点的next而就此断裂
			tmp=pHead.next 
			# 保存完next，就可以让pHead的next指向last
			pHead.next=last
			# 让last，pHead依次向后移动一个节点，继续下一次的指针反转
			last=pHead
			pHead=tmp 

		return last

	def ReverseList2(self, pHead):
		if pHead==None:
			return None
		last=None 

		while pHead:
			tmp=pHead.next 
			pHead.next=last
			last=pHead
			pHead=tmp
		return last

	def ReverseList3(self, pHead):

		if pHead==None:
			return None
		last=None
		while pHead:
			tmp=pHead.next
			pHead.next=last 
			last=pHead
			pHead=tmp
		return last

	def ReverseList4(self, pHead):

		if pHead==None:
			return None
		last=None

		while pHead:
			tmp=pHead.next
			pHead.next=last 
			last=pHead
			pHead=tmp
		return last

	def ReverseList5(self, pHead):
		if pHead==None:
			return None

		last=None
		while pHead:
			tmp=pHead.next
			pHead.next=last
			last=pHead
			pHead=tmp

		return last



def reverseVowels(s):
	if s==None or s=="":
		return

	tmp=[]
	list1=list(s)
	count=0
	
	for i in range(len(list1yuan=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])):
		if list1[i] in yuan:
			tmp.append(list1[i]) 
			list1[i]=""
			count+=1


	else:
		tmp=tmp[::-1]
		print(list1, tmp)
		index=0
		for i in range(len(list1)):
			if list1[i]=="":
				list1[i]=tmp[index]
				index+=1
	return "".join(list1)


print(reverseVowels("aA"))














node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

S = Solution()
# p = S.ReverseList(node1)
p = S.ReverseList3(node1)
print(p.data)














































