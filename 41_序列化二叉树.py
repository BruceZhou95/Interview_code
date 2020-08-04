'''
请实现两个函数，分别用来序列化和反序列化二叉树。这里没有规定序列化的方式。
'''

class TreeNode:
	def __init__(self, x):
		self.val=x
		self.left=None
		self.right=None

class Solution(object):
	def Serialize(self, root):
		serializeStr=""
		if root==None:
			return "#"
		stack=[]
		while root or stack:
			while root:
				serializeStr+=str(root.val)+","
				stack.append(root)
				root=root.left 
			serializeStr+="#" # 当左、右节点为null是以"#"结尾
			root=stack.pop() # 先把二叉树的左节点插入，然后通过pop出来再重新添加右节点，最后进行翻转才是前序遍历
			root=root.right
		serializeStr=serializeStr[::-1]
		return serializeStr

	def Deserialize(self, s):
		serialize=s.split(",")
		tree, sp=self.deserialize(serialize, 0)
		return tree 

	def deserialize(self, s, sp):
		if sp>=len(s) or s[sp]=="#":
			return None, sp+1
		node=TreeNode(int(s[sp]))
		sp+=1
		node.left, sp=self.deserialize(s, sp)
		node.right, sp=self.deserialize(s, sp)
		return node, sp 

	def Serialize1(self, root):
		serializeStr=""
		if root==None:
			return "#"
		stack=[]
		while root or stack:
			while root:
				serializeStr+=str(root.val)+","
				stack.append(root)
				root=root.left
			serializeStr+="#"
			root=stack.pop()
			root=root.right

		serializeStr=serializeStr[::-1]
		return serializeStr

	def Deserialize1(self, s):
		serialize=s.split(",")
		tree, sp=self.deserialize1(serialize, 0)
		return tree

	def deserialize1(self, s, sp):
		if sp>=len(s) or s[sp]=="#":
			return None ,sp+1
		node=TreeNode(int(s[sp]))
		sp+=1
		node.left, sp=self.deserialize1(s, sp)
		node.right, sp=self.deserialize1(s, sp)
		return node, sp 


		







































