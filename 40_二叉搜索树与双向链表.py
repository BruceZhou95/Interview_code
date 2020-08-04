'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''

class TreeNode(object):
	def __init__(self, x):
		self.val=x
		self.left=None 
		self.right=None


class Solution(object):
	def Convert(self, pRootOfTree):
		if pRootOfTree== None:
			return None 
		
		if not pRootOfTree.left and not pRootOfTree.right: # 当节点的左右子树都为空时，则返回根节点
			return pRootOfTree

		# 处理左子树
		self.Convert(pRootOfTree.left)
		left=pRootOfTree.left 

		# 链接根与左子树的最大节点
		if left:
			while left.right:
				left=left.right 
			pRootOfTree.left, left.right=left, pRootOfTree

		# 处理右子树
		self.Convert(pRootOfTree.right)
		right=pRootOfTree.right 

		# 连接根与右子树最小节点
		if right:
			while right.left:
				right=right.left
			pRootOfTree.right, right.left=right, pRootOfTree

		while pRootOfTree.left:
			pRootOfTree=pRootOfTree.left

		return pRootOfTree

	def Convert1(self, pHead):
		if not pHead:
			return None 
		if not pHead.left and not pHead.right:
			return pHead

		# 处理左子树
		self.Convert1(pHead.left)
		left=pHead.left 

		if left:
			while left.right:
				left=left.right 
			pHead.left, left.right=left, pHead

		# 处理右子树
		self.Convert1(pHead.right)
		right=pHead.right
		if right:
			while right.left:
				right=right.left
			pHead.right, right.left=right, pHead

		while pHead.left:
			pHead=pHead.left 

		return pHead

	def Convert2(self, pHead):
		if not pHead:
			return None 

		if not pHead.left and not pHead.right:
			return pHead

		# 处理左子树
		self.Convert2(pHead.left)
		left=pHead.left 

		if left:
			while left.right:
				left=left.right

			pHead.left, left.right=left, pHead


		# c处理右子树
		self.Convert2(pHead.right)
		right=pHead.left 

		if right:
			while right.left:
				right=right.left 

			pHead.right, right.left=right, pHead

		while pHead.left:
			pHead=pHead.left 

		return pHead


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
newList = S.Convert1(pNode1)
print(newList.val)




































