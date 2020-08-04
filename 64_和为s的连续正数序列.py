
'''
输入一个正数s,打印出所有和为s的连续正数序列(至少含有两个数)。例如，输入15，由于1+2+3+4+5=4+5+6=7+8=15，所以打印出3个连续序列1~5、4~6和7~8。
'''

class Solution(object):

	def FindContinuousSequence(self, Tsum):
		if Tsum<3:
			return []

		small=1
		big=2
		middle=(Tsum+1)//2 # small一直加到middle
		curSum=small+big
		output=[]
		while small<middle:
			if curSum==Tsum:
				output.append(list(range(small, big+1)))
			while curSum>Tsum and small<middle:
				curSum-=small
				small+=1
				if curSum==Tsum:
					output.append(list(range(small, big+1)))
			big+=1
			curSum+=big
		return output

	def FindContinuousSequence2(self, Tsum):
		if Tsum<3:
			return []
		small, big=1, 2
		middle=(Tsum+1)>>1
		curSum=small+big
		output=[]
		while small<middle:
			if curSum==Tsum:
				output.append(list(range(small, big+1)))
				big+=1
				curSum+=big 
			elif curSum>Tsum:
				curSum-=small
				small+=1
			else:
				big+=1
				curSum+=big
		return output

	def FindContinuousSequence21(self, Tsum):
		if Tsum<3:
			return []
		small, big=1,2
		middle=(Tsum+1)>>1
		curSum=small+big
		output=[]

		while small<middle:
			if curSum==Tsum:
				output.append(list(range(small, big+1)))
				big+=1
				curSum+=big
			elif curSum>Tsum:
				curSum-=small 
				small+=1
			else:
				big+=1
				curSum+=big
		return output

	def FindContinuousSequence22(self, Tsum):

		if Tsum<3:
			return []

		small, big=1, 2
		middle=(Tsum+1)>>1
		curSum=small+big 
		output=[]

		while small<middle:
			if curSum==Tsum:
				output.append(list(range(small, big+1)))
				big+=1
				curSum+=big
			elif curSum<Tsum:
				big+=1
				curSum+=big
			else:
				curSum-=small 
				small+=1
		return output


s=Solution()
print(s.FindContinuousSequence(15))
print(s.FindContinuousSequence21(15))
print(s.FindContinuousSequence22(15))











































