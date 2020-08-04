
'''
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''


class TreeNode(object):
	def __init__(self, x):
		self.val=x
		self.left=None 
		self.right=None 

class Solution(object):

	# 1.递归实现
	def isSymmetrical(self, pRoot):
		return self.selfIsSymmetrical(pRoot, pRoot)

	def selfIsSymmetrical(self, pRoot1, pRoot2):
		if pRoot1==None and pRoot2==None:
			return True
		if pRoot1==None or pRoot2==None:
			return False
		if pRoot1.val!=pRoot2.val:
			return False 

		return self.selfIsSymmetrical(pRoot1.left, pRoot2.right) and \
			self.selfIsSymmetrical(pRoot1.right, pRoot2.left)

	# 递归实现2
	def isSymmetrical1(self, pRoot):
		return self.selfIsSymmetrical(pRoot, pRoot)

	def selfIsSymmetrical1(self, pRoot1, pRoot2):

		if pRoot1==None and pRoot2==None:
			return True 

		if pRoot1==None or pRoot2==None:
			return False 

		if pRoot1.val!=pRoot2.val:
			return False 

		return self.selfIsSymmetrical(pRoot1.left, pRoot2.right) and \
			self.selfIsSymmetrical(pRoot1.right, pRoot2.left)

	def isSymmetrical2(self, pRoot):
		return self.selfIsSymmetrical(pRoot, pRoot)

	def selfIsSymmetrical2(self, pRoot1, pRoot2):
		if pRoot1==None and pRoot2==None:
			return True

		if pRoot1==None or pRoot2==None:
			return False 

		if pRoot1.val!=pRoot2.val:
			return False

		return self.selfIsSymmetrical(pRoot1.left, pRoot2.right) and \
			self.selfIsSymmetrical(pRoot1.right, pRoot2.left)



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
result = S.isSymmetrical2(pNode1)
print(result)




















































