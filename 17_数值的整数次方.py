

# 求一个数值的整数次方，不能使用库函数

class Solution(object):

	# 考虑的是exponent的取值
	def exponent(self, base, ex):
		result=1
		if ex==0:
			return 1
		
		elif ex<0:
			for i in range(abs(ex)):
				result=base*result

			return 1/result
		else:
			for i in range(ex):
				result=base*result
			return result

	def exponent1(self, base, ex):

		if ex==0:
			return 0
		elif ex==1:
			return base
		elif ex==-1:
			return 1/base

		result=self.exponent1(base, ex>>1)
		result*=result
		if (ex & 0x1==1):
			result*=base 
		return result

	def exponent2(self, base, ex):
		if ex==0:
			return 0
		elif ex==1:
			return base
		elif ex==-1:
			return 1/base
		result=self.exponent2(base, ex>>1)
		result*=result
		if (ex&0x1==1):
			result*=base 
		return result


	def exponent3(self, base, ex):
		if ex==0:
			return 0
		elif ex==1:
			return base 
		elif ex==-1:
			return 1/base 

		result=self.exponent3(base, ex>>1)
		result*=result
		if (ex%2==1):
			result *= base 
		return result


S=Solution()
print(S.exponent3(2, 5))




































