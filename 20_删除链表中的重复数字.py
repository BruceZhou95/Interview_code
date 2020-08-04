

'''
删除链表中重复的结点
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
'''

class ListNode(object):
	def __init__(self, x):
		self.data=x
		self.next=None

class Solution(object):

	def deleteDuplication(self, pHead):

		r"""
			Args:
				pHead:头结点
		"""
		if pHead==None:
			return 
		prehead=None # 当前节点的前一个节点
		pNode=pHead 
		while pNode!=None:
			needDelete=False 
			nextNode=pNode.next 
			if nextNode!=None and nextNode.data==pNode.data:
				needDelete=True 
			if needDelete==False:
				prehead=pNode
				pNode=pNode.next 
			else:
				nodeData=pNode.data
				pToBeDel = pNode
				while pToBeDel!=None and pToBeDel.data==nodeData:
					pToBeDel=pToBeDel.next 
				if prehead==None:
					pHead=pToBeDel
					pNode=pToBeDel
					continue
				else:
					prehead.next=pToBeDel
				pNode=prehead
		return pHead

	def deleteDuplication1(self, pHead):
		if pHead==None:
			return 
		preHead=None # 当前节点的前一个节点
		pNode=pHead # 将头结点赋值给pNode

		while pNode!=None:
			needDelete=False
			nextNode=pNode.next  # 当前节点pNode、当前节点的下一个节点nextNode
			if nextNode!=None and nextNode.data==pNode.data:
				needDelete=True 

			if needDelete==False:
				preHead=pNode
				pNode=pNode.next
			else:
				nodeData=pNode.data 
				pToBeDel=pNode
				while pToBeDel!=None and pToBeDel.data==nodeData:
					pToBeDel=pToBeDel.next
				if preHead==None:
					pHead=pToBeDel
					pNode=pToBeDel
					continue
				else:
					preHead.next=pToBeDel
				pNode=preHead
		return pHead

	def deleteDuplication2(self, phead):
		if pHead==None:
			return 
		preHead=None # 当前节点的前一个节点
		pNode=pHead 
		while pNode!=None:
			needDelete=False 
			nextNode=pNode.next 
			if nextNode!=None and nextNode.data==pNode.data:
				needDelete=True

			if needDelete==False:
				preHead=pNode
				pNode==pNode.next 
			else:
				nodeData=pNode.data 
				pToBeDel=pNode
				while pToBeDel!=None and pToBeDel.data==nodeData:
					pToBeDel=pToBeDel.next 
				if preHead==None:
					pHead=pToBeDel
					pNode=pToBeDel
					continue
				else:
					preHead.next=pToBeDel
				pNode=preHead
			return pHead


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution1:  # 递归
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead
        if pHead.data != pHead.next.data:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead   # 后面的节点递归结束后，返回pHead即可
        else:
            tempNode = pHead
            while tempNode and tempNode.data == pHead.data:
                tempNode = tempNode.next
            return self.deleteDuplication(tempNode)  
            # 重复节点都不留，不保留pHead，直接返回下一个不同节点的递归结点。

    def deleteDuplication1(self, pHead):
    	if pHead==None:
    		return None
    	if pHead.next==None:
    		return pHead 

    	if pHead.data!=pHead.next.data:
    		pHead.next=self.deleteDuplication1(pHead.next)
    		return pHead

    	else:
    		tempNode=pHead.next 
    		while tempNode and tempNode.data==pHead.data:
    			tempNode=tempNode.next 
    		return self.deleteDuplication1(tempNode)

    def deleteDuplication2(self, pHead):
    	if pHead==None:
    		return None 
    	if pHead.next==None:
    		return pHead 

    	if pHead.data!=pHead.next.data:
    		pHead.next=self.deleteDuplication2(pHead.next)
    		return pHead
    	else:
    		tempNode=pHead.next 
    		while tempNode and tempNode.data==pHead.data :
    			tempNode=tempNode.next 
    		return self.deleteDuplication2(tempNode)

    def deleteDuplication3(self, pHead):
    	if pHead==None:
    		return None 
    	if pHead.next==None:
    		return pHead 
    	if pHead.data!=pHead.next.data:
    		pHead.next=self.deleteDuplication3(pHead.next)
    		return pHead 
    	else:
    		tempNode=pHead.next 
    		while tempNode and tempNode.data==pHead.data:
    			tempNode=tempNode.next 
    		return self.deleteDuplication3(tempNode)

    def deleteDuplication4(self, pHead):

    	if pHead==None:
    		return None 
    	if pHead.next==None:
    		return pHead
    	if pHead.data!=pHead.next.data:
    		pHead.next=self.deleteDuplication4(pHead, pHead)
    		return pHead
    	else:
    		tempNode=pHead.next
    		while tempNode and tempNode.data==pHead.data:
    			tempNode=tempNode.next
    		return self.deleteDuplication4(tempNode)

    		
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:# 循环
    def deleteDuplication(self, pHead):
        # write code here
        first = ListNode(-1)     # 为了避免重复，在链表开始之前新建一个头结点。
        first.next = pHead
        curr = pHead   # 作为遍历链表的指针
        pre = first    # 记录不重复节点之前的最后信息
        while curr and curr.next:
            if curr.data != curr.next.data:  # 当前节点不重复，继续往下走
                curr = curr.next
                pre = pre.next
            else:      # 如果重复，找到不重复节点为止。
                data = curr.data
                while curr and curr.data == data:
                    curr = curr.next
                pre.next = curr  
                # 这里直接令pre.next等于第一个与当前元素不重复的节点即可，
                # 不用管这个节点也是重复节点，因为pre一定不重复，且被固定了下来，
                # 是不变的，如果这个节点也是重复节点，pre.next会再次更新。
        return first.next



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(4)
node7 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution1()
print(s.deleteDuplication(node1).next.next.data)









































