

# 给定二叉树的一个节点，给出中序遍历中该节点的下一个节点


# 给出树的定义
class TreeLinkNode(object):

	def __init__(self, data):
		self.data=data
		self.left=None
		self.right=None
		self.next=None

# 解决方法
class Solution(object):

	def GetNext(self, pNode):
		if pNode==None:
			return

		pNext=None # 保存下一个节点的值
		if pNode.right != None: # 判断右子树是否存在
			pRight=pNode.right 
			while pRight.left != None:
				pRight=pRight.left # 如果右子树的最左边那个节点存在，则下一个节点为右子树最左边的那一个节点
			pNext=pRight

		elif pNode.next!=None:
			pCurrent=pNode
			pParent=pCurrent.next 
			while pParent != None and pCurrent==pParent.right:
				pCurrent=pParent
				pParent=pCurrent.next 
			pNext=pParent
			
		return Pnext

class Solution2(object):

	def GetNext(self, pNode):
		#  如果输入是一个空节点
		if pNode==None:
			return None 

		# 注意当前节点是根节点的情况。所以在最开始假定pNext=None,
		# 如果下列情况都不满足，说明当前节点为根节点，直接输出None

		pNext=None  # 这里的pNode指的是头结点
		# 如果输入节点有右子树，则下一个节点是当前节点右子树中最左的节点
		if pNode.right:
			pNode=pNode.right 
			while pNode.left:
				pNode=pNode.left
			pNext=pNode

		else:
			#如果当前有父节点且当前节点是父节点的左子节点，下一个节点即为父节点
			if pNode.next and pNode.next.left==pNode:
				pNext=pNode.next

			# 如果当前节点有父节点且当前节点是父节点的右子节点, 那么向上遍历
            # 当遍历到当前节点为父节点的左子节点时, 输入节点的下一个结点为当前节点的父节点
       		 elif pNode.next and pNode.next.right==pNode:
       		 	pNode=pNode.next 

       		 	while pNode.next and pNode.next.right==pNode:
       		 		pNode=pNode.next

       		 	# 遍历终止时当前节点有父节点, 说明当前节点是父节点的左子节点, 输入节点的下一个结点为当前节点的父节点
                # 反之终止时当前节点没有父节点, 说明当前节点在位于根节点的右子树, 没有下一个结点

                if pNode.next:
                	pNext=pNode.next
        return pNext


class Solution32(object):

	def GetnextNode(self, pNode):
		if pNode==None:
			return Node 

		pNext=None

		if(pNode.right):
			pNode=pNode.right 
			while pNode.left:
				pNode=pNode.left
			pNext=pNode
		else:
			if pNode.next and pNode.next.left==pNode:
				pNext=pNode.next 

			elif pNode.next and pNode.next.right==pNode:
				pNode=pNode.next 
				while pNode.next and pNode.next.right==pNode:
					pNode=pNode.next 

				if pNode.next:
					pNext=pNode.next 

		return pNext 



class Solution42(object):

	def GetnextNode(self, pNode):
		if (pNode==None):
			return Node

		pNode=None 

		if(pNode.right):
			pNode=pNode.right 
			while(pNode.left):
				pNode=pNode.left 
			pNext=pNode
		else:
			if pNode.next and pNode.next.left==pNode:
				# pNode.next代表的是父节点 pNode代表当前节点
				pNext=pNode.next 

			elif pNode.next and pNode.next.right=pNode:
				pNode=pNode.next
				while pNode.next and pNode.next.right==pNode:
					pNode=pNode.next 


				if pNode.next:
					pNext=pNode.next 

		return pNext


class Solution52(object):

	def GetnextNode(self, Node):
		if pNode==None:
			return Node 

		pNext=None

		if(pNode.right):
			pNode=pNode.right
			while pNode.left:
				pNode=pNode.left 

		pNext=pNode

		else:

			if pNode.next and pNext.next.left==pNode:
				pNext=pNode.next 

			elif pNode.next and pNode.next.right==pNode:
				pNode=pNode.next
				while pNode.next and pNode.next.right==pNode:
					pNode=pNode.next 

				if pNode.next:
					pNext=pNode.next

		return pNext




















































