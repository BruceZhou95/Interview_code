

"""
将一个n绳子段的绳子剪成m段，使得每段的绳子乘积最大
例:长度3的绳子可以剪成1-1-2；1-2；和1-1-1但是，第1种减法和第2种剪发的乘积最大为2

"""

class Solution(object):

	# 使用动态规划
	def MaxMulti1(self, length):

		# 给出的方法是从f(1)、f(2)、f(3)
		if length<2:
			return 0
		if length==2:
			return 1
		if length==3:
			return 2

		products=[0]*(length+1)
		products[0]=0
		products[1]=1
		products[2]=2
		products[3]=3

		max=0
		for i in range(4, length+1):
			for j in range(1, (i//2)+1):
				product=products[j]*products[i-j]
				if max<product:
					max=product 
			products[i]=max
		max=products[length]

		return max 

	def MaxMulti11(self, length):

		if length<2:
			return 0
		if length==2:
			return 1
		if length==3:
			return 2

		products=[0]*(length+1)
		products[0]=0
		products[1]=1
		products[2]=2
		products[3]=3

		max=0
		for i in range(4, length+1):
			for j in range(1, (i//2+1)):
				product=products[j]*products[i-j]
				if(max<product):
					max=product 
			products[i]=max
			max=products[length]
		return max

	def MaxMutil12(self, length):

		if length<2:
			return 0
		if length==2:
			return 1
		if length==3:
			return 2

		products=[0]*(length+1)
		max=0
		product=0
		for i in range(4, length+1):
			for j in range(1, (i//2)+1):
				product=products[j]*products[i-j]
				if (max<product):
					max=product 
			products[i]=max 

		max=products[length]
		return max

	# 贪婪算法
	def MaxMulti2(self, length):
		if (length<2):
			return 0

		if(length==2):
			return 1

		if(length==3):
			return 2

		timesOf3=0
		timesOf3=length//3

		if(length-timesOf3*3==1):
			timesOf3-=1

		timesOf2=0
		timesOf2=(length-timesOf3*3)//2
		print(timesOf2, timesOf3)

		return pow(3, timesOf3)*pow(2, timesOf2)

	def MaxMulti21(self, length):
		if length<2:
			return 0
		if length==2:
			return 1
		if length==3:
			return 2

		timesOf3=length//3

		if(length-timesOf3*3==1):
			timesOf3-=1

		timesOf2=(length-timesOf3*3)//2

		return pow(3, timesOf3)*pow(2, timesOf2)






























S=Solution()

print(S.MaxMulti2(15))









































