'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''


class Solution(object):



	# 文中的第一种方法，时间消耗较大
	def isUgry(self, number):

		while number%2==0:
			number//=2
		while number%3==0:
			number//=3
		while number%5==0:
			number//=5
		return number==1

	def getUgryNumber(self, index):
		if index<=0:
			return index
		if index==1:
			return index

		number=0
		UgryNumver=0

		while UgryNumver<index:
			number+=1
			if self.isUgry(number):
				UgryNumver+=1

		return number
	# ******************************************************************
	# 第二种方法，以空间换时间
	def GetUalyNumber_solution(self, index):
		if index==None and len(index)<=0:
			return 0
		uglyNumbers=[1]*index
		nextIndex=1

		index2=0
		index3=0
		index5=0

		while nextIndex<index:
			minVal=min(uglyNumbers[index2]*2, uglyNumbers[index3]*3, 
				uglyNumbers[index5]*5)
			uglyNumbers[nextIndex]=minVal

			while uglyNumbers[index2]*2 <=uglyNumbers[nextIndex]:
				index2 += 1
			while uglyNumbers[index3]*3<=uglyNumbers[nextIndex]:
				index3+=1
			while uglyNumbers[index5]*5<=uglyNumbers[nextIndex]:
				index5+=1
			nextIndex+=1
		return uglyNumbers[-1]

	def GetUrlyNumber_solution1(self, index):
		if index==None or len(index)<=0:
			return 0

		uglyNumbers=[1]*index 
		nextIndex=1

		index2=0
		index3=0
		index5=0

		while nextIndex<index:
			minVal=min(uglyNumbers[index2]*2, uglyNumbers[index3]*3, 
				uglyNumbers[index5]*5)
			uglyNumbers[nextIndex]=minVal

			while uglyNumbers[index2]*2<=uglyNumbers[nextIndex]:
				index2+=1
			while uglyNumbers[index3]*3<=uglyNumbers[nextIndex]:
				index3+=1
			while uglyNumbers[index5]*5<=uglyNumbers[nextIndex]:
				index5+=1
			nextIndex+=1

		return uglyNumbers[-1]

	def GetUrlyNumber_solution2(self, index):
		if index==None or index<=0:
			return 0

		uglyNumbers=[1]*index
		nextIndex=1

		index2=0
		index3=0
		index5=0

		while nextIndex<index:
			minVal=min(uglyNumbers[index2]*2, uglyNumbers[index3]*3, 
				uglyNumbers[index5]*5)
			uglyNumbers[nextIndex]=minVal

			while uglyNumbers[index2]*2<=uglyNumbers[nextIndex]:
				index2+=1
			while uglyNumbers[index3]*3<=uglyNumbers[nextIndex]:
				index3+=1
			while uglyNumbers[index5]*5<=uglyNumbers[nextIndex]:
				index5+=1
			nextIndex+=1

		return uglyNumbers[-1]


	def GetUrlyNumber_solution3(self, index):
		if index==None or index<=0:
			return 0

		uglyNumbers=[1]*index
		nextIndex=1

		index2=0
		index3=0
		index5=0

		while nextIndex<index:
			minVal=min(uglyNumbers[index2]*2, uglyNumbers[index3]*3, 
				uglyNumbers[index5]*5)
			uglyNumbers[nextIndex]=minVal

			while uglyNumbers[index2]<=uglyNumbers[nextIndex]:
				index2+=1
			while uglyNumbers[index3]<=uglyNumbers[nextIndex]:
				index3+=1
			while uglyNumbers[index5]<=uglyNumbers[nextIndex]:
				index5+=1
			nextIndex+=1

		return uglyNumbers[-1]

	def GetUrlyNumber_solution4(self, index):
		if index==None or index<=0:
			return 0

		uglyNumbers=[1]*index 
		nextIndex=1

		index2=0
		index3=0
		index5=0

		while nextIndex<index:
			minVal=min(uglyNumbers[index2]*2, uglyNumbers[index3]*3, 
				uglyNumbers[index5]*5)
			uglyNumbers[nextIndex]=minVal
			while uglyNumbers[index2]*2<=uglyNumbers[nextIndex]:
				index2+=1
			while uglyNumbers[index3]*3<=uglyNumbers[nextIndex]:
				index3+=1
			while uglyNumbers[index5]*5<=uglyNumbers[nextIndex]:
				index5+=1
			nextIndex+=1
		return uglyNumbers[-1]

	def GetUrlyNumber_solution5(self, index):
		if index==None or index<=0:
			return 0

		uglyNumbers=[1]*index 
		nextIndex=1

		index2=0
		index3=0
		index5=0

		while nextIndex<index:
			minVal=min(uglyNumbers[index2]*index2, uglyNumbers[index3]*3, 
				uglyNumbers[index5]*5)
			uglyNumbers[nextIndex]=minVal
			while uglyNumbers[index2]*2<=uglyNumbers[nextIndex]:
				index2+=1
			while uglyNumbers[index3]*3<=uglyNumbers[nextIndex]:
				index3+=1
			while uglyNumbers[index5]*5<=uglyNumbers[nextIndex]:
				index5+=1
			nextIndex+=1
		return uglyNumbers[-1]

s=Solution()
# print(s.isUgry(11))
# print(s.getUgryNumber(11))
print(s.GetUalyNumber_solution(11))
















































