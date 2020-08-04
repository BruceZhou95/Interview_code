
'''
操作给定的二叉树，将其变换为源二叉树的镜像。
'''


class TreeNode(object):

	def __init__(self, x):
		self.val=x
		self.left=None
		self.right=None 

class Solution(object):

	# 递归实现
	def Mirror(self, root):
		if root==None:
			return 

		if root.left==None and root.right==None:
			return root 

		root.left, root.right=root.right, root.left

		self.Mirror(root.left)
		self.Mirror(root.right)

	# 非递归实现

	def Mirror1(self, root):
		if root==None:
			return 

		stackNode=[] # 定义一个列表存储树的节点
		stackNode.append(root)
		while len(stackNode)>0:
			nodeNum=len(stackNode)-1
			tree=stackNode[nodeNum]
			stackNode.pop()
			nodeNum-=1
			if tree.left!=None or tree.right!=None:
				tree.left, tree.right=tree.right, tree.left 

			if tree.left:
				stackNode.append(tree.left)
				nodeNum+=1
			if tree.right:
				stackNode.append(tree.right)
				nodeNum+=1

	# 非递归实现
	def MirrorNoRecursion(self, root):
		if root==None:
			return 
		nodeQue=[root]
		while len(nodeQue)>0:
			curLevel, count=len(nodeQue), 0
			while count<curLevel:
				count+=1
				pRoot=nodeQue.pop(0)
				pRoot.left, pRoot.right=pRoot.right, pRoot.left
				if pRoot.left:
					nodeQue.append(pRoot.left)
				if pRoot.right:
					nodeQue.append(pRoot.right)

	def MirrorNoRecursion1(self, root):
		if root==None:
			return 
		nodeQue=[root]
		while len(nodeQue)>0:
			curLevel, count=len(nodeQue), 0
			while count<curLevel:
				count+=1
				pRoot=nodeQue.pop(0)
				pRoot.left, pRoot.right=pRoot.right, pRoot.left
				if pRoot.left:
					nodeQue.append(pRoot.left)
				if pRoot.right:
					nodeQue.append(pRoot.right)

	def MirrorNoRecursion2(self, root):
		if root==None:
			retrun 
		nodeQue=[root] # 存放将要遍历的节点
		while len(nodeQue)>0:
			curLevel, count=len(nodeQue), 0
			while count<curLevel:
				count+=1
				pRoot=nodeQue.pop(0)
				pRoot.left, pRoot.right=pRoot.right, pRoot.left
				if pRoot.left:
					nodeQue.append(pRoot.left)
				if pRoot.right:
					nodeQue.append(pRoot.right)

	def MirrorNoRecursion3(self, root):
		if pRoot==None:
			return 
		nodeQue=[root]
		curLevel, count=len(nodeQue), 0
		while len(nodeQue):
			count+=1
			pRoot=nodeQue.pop(0)
			pRoot.left, pRoot.right=pRoot.right, pRoot.left
			if pRoot.left:
				nodeQue.append(pRoot.left)
			if pRoot.right:
				nodeQue.append(pRoot.right)

	def MirrorNoRecursion6(self, root):
		if root==None:
			return

		nodeQue=[root]
		
		while len(nodeQue)>0:
			curLevel, count=len(nodeQue), 0
			while count<curLevel:
				count+=1
				pRoot=root.pop(0)
				pRoot.left, pRoot.right=pRoot.right, pRoot.left
				if pRoot.left:
					nodeQue.append(pRoot.left)
				if pRoot.right:
					nodeQue.append(pRoot.right)

	def MirrorNoRecursion7(self, root):
		if root==None:
			return 
		nodeQue=[root]
		while len(nodeQue)>0:
			curLevel, count=len(nodeQue), 0
			print("*"*10)
			while count<curLevel:
				count+=1
				pRoot=nodeQue.pop(0)
				print(count, curLevel)
				pRoot.left, pRoot.right=pRoot.right, pRoot.left

				if pRoot.left:
					nodeQue.append(pRoot.left)
				if pRoot.right:
					nodeQue.append(pRoot.right)

		print("*"*20)


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
# S.Mirror1(pNode1)
S.MirrorNoRecursion7(pNode1)
print(pNode1.val)









































