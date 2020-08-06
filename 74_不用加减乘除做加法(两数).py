
"""
题目:写一个函数，求两个整数之和，要求在函数体内不得使用"+"、"-"、"*"、"/"四则运算符号。
"""

class Solution(object):

	def Add(self, num1, num2): # 不行，可能无限循环
		sumT, carry=0, 0
		while num2:
			sumT=num1^num2
			carry=(num1&num2)<<1
			num1=sumT
			num2=carry
			# print(num2)
		print("Hello!")
		return num1

	def Add(self, num1, num2):
		sumT, carry=0, 0
		while num2:
			sumT=num1^num2
			carry=(num1&num2)<<1
			num1=sumT
			num2=carry
		print("Hello")
		return num1

	def Add1(self, num1, num2):# 使用了减法
		while num2:
			temp=num1 ^ num2 # 异或 相当于进行相加，但是，不进位
			num2=(num1 & num2)<<1 # 进位的话就左移
			num1=temp & (pow(2,32)-1)
			# num1=temp & 0xFFFFFFFF
		return num1 if num1>>31==0 else num1-pow(2,32)

	def Add2(self, num1, num2): # 可行

		x = pow(2, 32)-1
		num1, num2 = num1 & x, num2 & x
		while num2:
			num1, num2 = (num1 ^ num2), (num1 & num2) << 1 & x
		return num1 if num1 <= pow(2, 32)/2-1 else ~(num1 ^ x)

	def Add3(self, num1, num2):
		x=pow(2,32)-1
		num1, num2= num1&x, num2&x
		while num2:
			num1, num2=num1^num2, (num1&num2)<<1&x
		return num1 if num1<=pow(2, 32)/2-1 else ~(num1^x)

	def Add4(self, num1, num2):
		x=pow(2, 32)-1
		num1, num2=num1&x, num2&x
		while num2:
			num1, num2=num1^num2, (num1&num2)<<1&x
		return num1 if num1<=pow(2,32)/2-1 else ~(num1^x)

	def Add5(self, num1, num2):
		x=pow(2, 32)-1
		num1, num2=num1&x, num2&x
		while num2:
			num1, num2=num1^num2, (num1&num2)<<1&x
		return num1 if num1<=pow(2, 32)/2-1 else ~(num1^x)

s=Solution()
print(s.Add(-5, -4))
print(s.Add2(-5, -4))
print(s.Add3(-5, -4))
print(s.Add4(-5, -4))



def tt():
	a,b=1,3
	if a>0:
		return (a and b)

# print(tt())


















































