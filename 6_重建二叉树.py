
# 根据二叉树的前序遍历和中序遍历来重建二叉树
# 假设输入的数据不含重复的数字
# 输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

class TreeNode(object):
	def __init__(self, data):
		self.data=data
		self.left=None
		self.right=None

class Solution(object):

	def reConstructBinaryTree(self, pre, tin):
		r"""
		Args:
			pre:前序遍历
			tin:中序遍历
		"""
		if not pre and not tin:
			return None
		root=TreeNode(pre[0])

		if set(pre)!=set(tin): # 判断是否包含重复的数字
			return None

		i=tin.index(pre[0]) # 确定根节点在中序遍历中的位置
		root.left=self.reConstructBinaryTree(pre[1:i+1], tin[:i])
		root.right=self.reConstructBinaryTree(pre[i+1:], tin[i+1:])
		return root 


pre = [1, 2, 3, 5, 6, 4] # 前序遍历
tin = [5, 3, 6, 2, 4, 1] # 中序遍历
test = Solution()
newTree = test.reConstructBinaryTree(pre, tin)


# 按层序序遍历输出某一层的值
def PrintNodeAtLevel(tree, level): # 这里的层数从0开始计算
	if not tree or level<0:
		return 0
	if level==0:
		print(tree.data)
		return 1
	PrintNodeAtLevel(tree.left, level-1)
	PrintNodeAtLevel(tree.right, level-1)

# 一直树的深度，按层输出数的值

def PrintNodeByLevel(treeNode, depath): # 这里的深度从1开始计算
	for level in range(depath):
		PrintNodeByLevel(treeNode, level)

PrintNodeAtLevel(newTree, 3)


#————————————————————————————————————————————————————————————————————————————————————————————————————

class TreeNode1(object): # 定义树
	
	def __init__(self, data):
		self.data=data
		self.left=left 
		self.right=right 

class Solution1(object): # 
	
	def reConstructBinaryTree1(self, pre, tin):

		if not pre and not tin:
			return None

		if set(pre) != set(tin):
			return None

		root=TreeNode1(pre[0])

		i=tin.index(pre[0])

		root.left=self.reConstructBinaryTree1(pre[1:i+1], tin[:i])
		root.right=self.reConstructBinaryTree1(pre[i+1:], tin[i+1:])

		return root 


pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]

test=Solution1()
tree=test.reConstructBinaryTree1(pre, tin)

def PrintNodeAtLevel(tree, level):

	if not tree or level<0:
		return 0
	if level==0:
		print(tree.data)
		return 1
	PrintNodeAtLevel(tree.left, level-1)
	PrintNodeAtLevel(tree.right, level-1)

def PrintNodeByLevel(tree, levels):
	for level in range(levels):
		PrintNodeAtLevel(tree, level)

#————————————————————————————————————————————————————————————————————————————————————————————————————

# 定义树
class TreeNode2(object):

	def __init__(self, data):
		self.data=data
		self.left=None
		self.right=None 

class Solution2(object):

	def reConstructBinaryTree2(self, pre, tin):

		if not pre and not tin:
			return None 

		if set(pre)!=set(tin):
			return None 

		root=TreeNode2(pre[0])

		i=tin.index(pre[0])
		root.left=self.reConstructBinaryTree2(pre[1:i+1], tin[:i])
		root.right=self.reConstructBinaryTree2(pre[i+1:], tin[i+1])
		return root 

pre = [1, 2, 3, 5, 6, 4]
tin = [5, 3, 6, 2, 4, 1]
test = Solution2()
newTree = test.reConstructBinaryTree2(pre, tin)

# 输出树的第几层
def PrintNodeAtLevel2(tree, level):

	if not tree or level<0:
		return 1
	if level==0:
		print(tree.data)
		return 1 
	PrintNodeAtLevel(tree, level-1)
	PrintNodeAtLevel(tree, leve-1)

def PrintNodeByLevel2(tree, depath):
	for level in range(depath):
		PrintNodeAtLevel(tree, level)

	


































