
# 判断输入整数的二进制中1的个数

def tes(n):
	strbinary=bin(n)
	intBinary=int(strbinary[2:])

	count=0
	print(intBinary)
	while intBinary:
		i=intBinary%10
		if(i==1):
			count+=1
		intBinary=intBinary//10

	return count


# print(tes(80))


class Solution(object):

	def CountNum1(self, number):
		count=0

		while number:
			if number&1: # 判断是否是奇数
				count+=1
			number=number>>1
		print(count)

	def CountNum2(self, number):

		count=0
		while (number):
			count+=1
			number=(number-1)&number
		return count

	

	# 输入m,判断需要改变m二进制中的多少位才能变成m
	def ChangeNum(self, m, n):

		a=m^n
		return self.CountNum1(a)


S=Solution()

print(S.CountNum2(80))
print(S.CountNum1(80))
# print(S.ChangeNum(100, 13))











