
'''
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票-次可能获得的最大利润是多少?例如，一只股票在某些时间节点的价格为{9, 11,8,5, 7, 12, 16, 14}。如果我们能在价格为5的时候买入并在价格为16时卖出，则能收获最大的利润11。
'''

class Solution(object):

	def MaxShares(self, nums):

		if not nums or len(nums)<2:
			return 0

		minV=nums[0]
		maxV=nums[1]-minV

		for i in range(2, len(nums)):
			if nums[i-1]<minV:
				minV=nums[i-1]

			if nums[i]-minV>maxV:
				maxV=nums[i]-minV

		return maxV

	def MaxShares1(self, nums):
		if not nums or len(nums)<2:
			return 0

		minV=nums[0]
		maxV=nums[1]-minV

		for i in range(2, len(nums)):
			if nums[i-1]<minV:
				minV=nums[i-1]
			if nums[i]-minV>maxV:
				maxV=nums[i]-minV

		return maxV

s=Solution()
print(s.MaxShares([9,11,8,5, 7, 12, 16, 14]))



























































