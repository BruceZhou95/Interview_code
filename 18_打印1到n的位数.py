
# 给定一个数n,打印从1到最大n的位数


class Solution(object):

	def Print1toN1(self, n):

		a=[]
		for i in range(1, int("9"*n)+1):
			a.append(i)

		return a

	def Print1toN2(self, n):

		a=[]
		num=0
		for i in range(n):
			num+=(10**i)*9

		for i in range(1, num+1):
			a.append(i)
		return a 

	def Print1toN3(self, n):

		a=[]
		for i in range(1, 10**n):
			a.append(i)
		return a

	def Print1toN4(self, n):

		if n<=0:
			return 
		number=['0']*n 
		while not self.Increment(number):
			self.PrintNumber(number)

	def Increment(self, number):
		isOverflow=False
		nTakeOver=0
		nLength=len(number)

		for i in range(nLength-1, -1, -1):
			nSum=int(number[i])+nTakeOver
			if i==nLength-1:
				nSum+=1

			if nSum>=10:
				if i==0:
					isOverflow=True
				else:
					nSum-=10
					nTakeOver=1
					number[i]=str(nSum)

			else:
				number[i]=str(nSum)
				break

		return isOverflow

	def PrintNumber(self, number):
		isBeginning0=True
		nLength=len(number)

		for i in range(nLength):
			if isBeginning0 and number[i] != '0':
				isBeginning0=False 
			if not isBeginning0:
				print("%c"%number[i], end="")
		print(' ', end="")


	def Print1toN5(self, n):
		if n<=0:
			return 

		number=['0']*n
		for i in range(10):
			number[0]=str(i)
			self.Print1toN5Rec(number, n, 0)

	def Print1toN5Rec(self, number, length, index):
		if index==length-1:
			self.PrintNumber(number)
			return 
		for i in range(10):
			number[index+1]=str(i)
			self.Print1toN5Rec(number, length, index+1)


S=Solution()
# print(S.Print1toN1(2))
# print(S.Print1toN2(2))
# print(S.Print1toN3(2))
S.Print1toN5(200)



































