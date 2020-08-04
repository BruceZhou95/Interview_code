'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''

class TreeNode(object):

	def __init__(self, x):
		self.val=x
		self.left=None
		self.right=None 

class Solution(object):

	def __init__(self):
		self.flag=True 

	def IsBalance_Solution(self, pRoot):
		self.getDepth(pRoot)
		return self.flag

	def getDepth(self, pRoot):
		if pRoot==None:
			return 0
		left=1+self.getDepth(pRoot.left)
		right=1+self.getDepth(pRoot.right)

		if abs(left-right)>1:
			self.flag=False
		return left if left>right else right 

	def getDepth(self, pRoot):
		if not pRoot:
			return 0
		left=1+self.getDepth(pRoot.left)
		right=1+self.getDepth(pRoot.right)

		if abs(left-right)>1:
			self.flag=False
		return left if left>right else right 

	def IsBalance_Solution1(self, pRoot):
		if pRoot==None:
			return True
		if abs(self.getDepth1(pRoot.left)-self.getDepth1(pRoot.right))>1:
			return False
		return self.IsBalance_Solution1(pRoot.left) and self.IsBalance_Solution1(pRoot.right)

	def getDepth1(self, root):
		if not root:
			return None 
		return max(self.getDepth1(root.left), self.getDepth1(root.right))+1





pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.right = pNode6
pNode5.left = pNode7

S = Solution()
print(S.IsBalance_Solution(pNode1))
print(S.getDepth(pNode1))
print(S.getDepth(pNode1))



































