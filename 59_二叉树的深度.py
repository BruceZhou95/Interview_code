
'''
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''
class TreeNode(object):
	def __init__(self, x):
		self.val=x
		self.left=None
		self.right=None

class Solution(object):

	# 递归算法
	def TreeDepath(self, root):
		if not pRoot:
			return 0

		else:
			return max(self.TreeDepath(root.left), self.TreeDepath(root.right))+1


	# 非递归算法，利用一个栈以及一个标志位栈
	def TreeDepth2(self, pRoot):
		if not pRoot:
			return 0

		depth=0
		stack, tag=[], []
		pNode=pRoot
		while pNode or stack:
			while pNode:
				stack.append(pNode)
				tag.append(0)
				pNode=pNode.left 

			if tag[-1]==1:
				depth=max(depth, len(stack))
				stack.pop()
				pNode=None 

			else:
				pNode=stack[-1]
				pNode=pNode.right
				tag.pop()
				tag.append(1)
		return depth

	def TreeDepth1(self, root):
		if not root:
			return 0
		else:
			return max(self.TreeDepth1(root.left), self.TreeDepth1(root.right))+1

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
print(S.TreeDepth2(pNode1)) # 有错误
print(S.TreeDepth1(pNode1))















































