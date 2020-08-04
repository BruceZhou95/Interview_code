'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
'''

class Solution(object):

	# O(nlogk)的算法, 适合海量数据
	# 利用一个k容量的容器存放数组, 构造最大堆, 当下一个数据大于最大数, 跳过, 小于最大数, 则进入容器替换之前的最大数
	def GetLeastNumbers(self, tinput, k):
		import heapq
		if tinput==None or len(tinput)<k or len(tinput)<=0 or k<=0:
			return []
		output=[]
		for number in tinput:
			if len(output)<k:
				output.append(number)
			else:
				output=heapq.nlargest(k, output)
				if number>=output[0]:
					continue
				else:
					output[0]=number

		return output[::-1]

	def GetLeastNumbers1(self, tinput, k):
		import heapq

		if tinput==None or len(tinput)<k or k<=0:
			return []
		output=[]

		for number in tinput:
			if len(output)<k:
				output.append(number)

			output=heapq.nlargest(k, output)
			if number>=output[0]:
				continue
			else:
				output[0]=number

		return output[::-1]

tinput = [4,5,1,6,2,7,3,8]
s = Solution()
# print(s.GetLeastNumbers_Solution(tinput, 4))
print(s.GetLeastNumbers(tinput, 4))
print(s.GetLeastNumbers(tinput, 5))







































