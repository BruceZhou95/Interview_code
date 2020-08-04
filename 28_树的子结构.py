
'''
输入两棵二叉树A，B，判断B是不是A的子结构
空树不是任意一个树的子结构
'''

class TreeNode(object):

	def __init__(self, x):
		self.val=x
		self.left=None
		self.right=None

class Solution(object):

	def HasSubtree(self, pRoot1, pRoot2):
		result=False
		if pRoot1 != None and pRoot2!=None:
			if pRoot1.val==pRoot2.val:
				result=self.DoesTree1haveTree2(pRoot1, pRoot2)
			if not result:
				result=self.HasSubtree(pRoot1.left, pRoot2)
			if not result:
				result=self.HasSubtree(pRoot1.right, pRoot2)

		return result
		# 用于递归判断树的每个节点是否相同
    # 需要注意的地方是: 前两个if语句不可以颠倒顺序
    # 如果颠倒顺序, 会先判断pRoot1是否为None, 其实这个时候pRoot2的结点已经遍历完成确定相等了, 但是返回了False, 判断错误
	def DoesTree1haveTree2(self, pRoot1, pRoot2):
	   	if pRoot2==None:
	   		return True 
	   	if pRoot1==None:
	   		return False
	   	if pRoot1.val!=pRoot2.val:
	   		return False

	   	return self.DoesTree1haveTree2(pRoot1.left, pRoot2.left) and \
	   	 self.DoesTree1haveTree2(pRoot1.right, pRoot2.right)

	def HasSubtree1(self, pRoot1, pRoot2):
		result=False
		if pRoot1.val!=None and pRoot2!=None:
			if pRoot1.val==pRoot2.val:
				result=self.DoesTree1haveTree21(pRoot1, pRoot2)

			if not result:
				result=self.HasSubtree(pRoot1.left, pRoot2)
			if not result:
				result=self.HasSubtree(pRoot1.right, pRoot2)

		return result

	def DoesTree1haveTree21(self, pRoot1, pRoot2):
		if pRoot2==None:
			return True 
		if pRoot1==None:
			return False 

		if pRoot1.val!=pRoot2.val:
			return False 

		return self.DoesTree1haveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1haveTree2(pRoot1.right, pRoot2.right)

	def HasSubtree2(self, pRoot1, pRoot2):
		result=False
		if pRoot1.val!=None and pRoot2.val!=None:
			if pRoot1.val==pRoot2.val:
				result=self.DoesTree1haveTree22(pRoot1, pRoot2)

			if not result:
				result=self.HasSubtree2(pRoot1.left, pRoot2)
			if not result:
				result=self.HasSubtree2(pRoot1.right, pRoot2)

		return False

	def DoesTree1haveTree22(self, pRoot1, pRoot2):
		if pRoot2==None:
			return True
		if pRoot1==None:
			return False
		if pRoot1.val!=pRoot2.val:
			return False 

		return self.DoesTree1haveTree22(pRoot1.left, pRoot2.left) and self.DoesTree1haveTree22(pRoot1.right, pRoot2.right)

	def HasSubtree3(self, pRoot1, pRoot2):
		result=False

		if pRoot1.val!=None and pRoot2.val!=None:
			if pRoot1.val==pRoot2.val:
				result=self.DoesTree1haveTree23(pRoot1, pRoot2)
			if not result:
				result=self.HasSubtree3(pRoot1.left, pRoot2)
			if not result:
				result=self.HasSubtree3(pRoot1.right, pRoot2)

		return result 

	def DoesTree1haveTree23(self, pRoot1, pRoot2):
		if pRoot2==None:
			return True
		if pRoot1==None:
			return False 

		if pRoot1.val!=pRoot2.val:
			return False

		return self.DoesTree1haveTree23(pRoot1.left, pRoot2.left) and self.DoesTree1haveTree23(pRoot1.right, pRoot2.right)

	def HasSubtree4(self, pRoot1, pRoot2):
		result=False 

		if pRoot1!=None and pRoot2!=None:
			if pRoot1.val==pRoot2.val:
				result= self.DoesTree1haveTree24(pRoot1, pRoot2)
			if not result:
				result=self.HasSubtree4(pRoot1.left, pRoot2)
			if not result:
				result.self.HasSubtree4(pRoot1.right, pRoot2)
		return result

	def DoesTree1haveTree24(self, pRoot1, pRoot2):
		if pRoot2==None:
			return True
		if pRoot1==None:
			return False
		if pRoot1.val!=pRoot2.val:
			return False 

		return self.DoesTree1haveTree24(pRoot1.left, pRoot2.left) and \
	self.DoesTree1haveTree24(pRoot2.left, pRoot2.right)



	def HasSubtree5(self, pRoot1, pRoot2):
		result=False 

		if pRoot1!=None and pRoot2!=None:
			if pRoot1.val==pRoot2.val:
				result=self.DoesTree1haveTree25(pRoot1, pRoot2)
			if not result:
				result=self.HasSubtree5(pRoot1.left, pRoot2)
			if not result:
				result=self.HasSubtree5(pRoot1.right, pRoot2)
		return result

	def DoesTree1haveTree25(self, pRoot1, pRoot2):
		if pRoot2==None:
			return True
		if pRoot1==None:
			return False 
		if pRoot1.val!=pRoot2.val:
			return False 

		return self.DoesTree1haveTree25(pRoot1.left, pRoot2.left) and \
			self.DoesTree1haveTree25(pRoot1.right, pRoot2.right)


pRoot1 = TreeNode(8)
pRoot2 = TreeNode(8)
pRoot3 = TreeNode(7)
pRoot4 = TreeNode(9)
pRoot5 = TreeNode(2)
pRoot6 = TreeNode(4)
pRoot7 = TreeNode(7)
pRoot1.left = pRoot2
pRoot1.right = pRoot3
pRoot2.left = pRoot4
pRoot2.right = pRoot5
pRoot5.left = pRoot6
pRoot5.right = pRoot7

pRoot8 = TreeNode(2)
pRoot9 = TreeNode(4)
pRoot10 = TreeNode(8)
pRoot8.left = pRoot9
pRoot8.right = pRoot10

S = Solution()
print(S.HasSubtree(pRoot1, pRoot8))


		

class B(Exception):
	def run():
		print("B")

class C(B):
	def run2():
		print("C")

class D(C):
	def run2():
		print("D")


for i in [D, C, B]:
	i.run2()

	








































