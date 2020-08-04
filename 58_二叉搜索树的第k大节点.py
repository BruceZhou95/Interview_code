r'''
给定一颗二叉搜索树，请找出其中的第k大的结点。例如，
     5
   /   \
  3     7
 / \   / \
2   4 6   8 中，
按结点数值大小顺序第三个结点的值为4。
'''
# 采用中序遍历的方法

class TreeNode(object):
	def __init__(self, x):
		self.val=x
		self.left=None
		self.right=None


class Solution(object):
	def __init__():
		self.treenode=[]

	def InOrder(self, root):# 中序遍历
		if root.left:
			self.treenode.append(root.left)
		self.treenode.append(root.val)
		if root.right:
			self.treenode.append(root.right)

	def KthNode(self, root, k):
		if k==0 or root=None:
			return 
		self.InOrder(root)
		if len(self.treenode)<k:
			return None 

		return self.treenode[k-1]

	# ************************************************************************

	def preOrder(self, root): # 前序遍历 练习
		if root==None:
			return None 

		self.treenode.append(root)
		if root.left:
			self.treenode.append(root.left)
		if root.right:
			self.treenode.append(root.right)

	def KthNode1(self, root, k):
		if root==None or k==0:
			return None 
		self.preOrder(root)

		if len(self.treenode)<k:
			return 0
		return self.treenode[k-1]

	def postOrder(self, root): # 后序遍历练习
		if root==None:
			return 
		if root.left:
			self.treenode(root.left)
		if root.right:
			self.treenode(root.right)
		self.treenode.append(root)

	def KthNode2(self, root, k):
		if root==None:
			return None 

		self.postOrder(root)
		if len(self.treenode)<k:
			return 0
		return self.treenode[k-1]










































