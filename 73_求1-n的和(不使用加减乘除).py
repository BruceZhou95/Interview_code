
'''
求1+2+...+n,要求不能使用乘除法、for、while、if. else、switch、case等关键字及条件判断语句(A?B:C)。
'''

class Solution(object):

	# def Sum_Solution(self, n):
	# 	return self.sumN(n)

	def sum0(self, n):
		return 0 

	# 利用非0值作两次非运算返回False，0作两次非运算返回True
	def sumN(self, n):

		fun={False:self.sum0, True:self.sumN}
		# 此处的fun[not not n] 不能写作func[not not n-1], 否则测试用例为0的话, 就会无限次迭代
		return n+fun[not not n](n-1)

	def sum0_1(self, n):
		return 0

	def sumN_1(self, n):
		fun={False:self.sum0_1, True:self.sumN_1}
		return n+fun[not not n](n-1)

	def sum0_2(self, n): # n必须加
		return 0

	def sumN_2(self, n):
		fun={False:self.sum0_2, True:self.sumN_2}
		return n+fun[not not n](n-1)

	def sum0_3(self, n):
		return 0

	def sumN_3(self, n):
		fun={False:self.sum0_3, True:self.sumN_3}
		return n+fun[not not n](n-1)

	def sum0_4(self, n):
		return 0

	def sumN_4(self, n):
		fun={False:self.sum0_4, True:self.sumN_4}
		return n+fun[not not n](n-1)

	def Sum_Solution2(self, n):
		return n and self.Sum_Solution(n-1)+n 

s=Solution()
# print(s.Sum_Solution(5))
print(s.sumN_2(5))
# print(s.Sum_Solution2(5))


















































