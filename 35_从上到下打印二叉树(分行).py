
'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''

class TreeNode(object):
	def __init__(self, x):
		self.val=x
		self.left=None
		self.right=None

class Solution(object):

	def levelOrder(self, pRoot):
		if not pRoot:
			return []

		nodes, res=[pRoot], [] # 
		while nodes:
			curStack, nextStack=[], []
			for node in nodes:
				curStack.append(node.val)
				if node.left:
					nextStack.append(node.left)
				if node.right:
					nextStack.append(node.right)
			res.append(curStack)
			nodes=nextStack
		return res 

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
aList = S.levelOrder(pNode1)
print(aList)







































