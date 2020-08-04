'''
1.数字在排序数组中出现的次数。统计一个数字在排序数组中出现的次数。例如，输入排序数组{1,2, 3,3,3,3,4, 5}和数字3，由于3在这个数组中出现了4次，因此输出4。
'''
class Solution(object):

	def GetFirstK(self, arr, k):
		start=0
		end=len(arr)-1
		res=[]

		while start<=end:
			middle=(start+end)//2
			if arr[middle]==k:
				i=middle
				j=middle
				while 0<=i-1<=end and arr[i-1]==k:
					res.append(i-1)
					i-=1
				res.append(middle)
				while 0<=j+1<=end and arr[j+1]==k:
					res.append(j+1)
					j+=1
				return  res
			elif arr[middle]<k:
				start=middle+1
			else:
				end=middle-1

s=Solution()
print(s.GetFirstK([1,2,3,3,3,3,4,5], 3))

'''
2.:0~n-1中缺失的数字。一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0~n-1之内。在范围0~n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
'''
class Solution(object):
	def missingNumber(self, nums):
		if not nums or len(nums)<=0:
			return None 

		if len(nums)==nums[-1]+1:
			return nums[-1]+1     

		maxValue=max(nums)
		N=sum(nums)
		M=(maxValue)*(maxValue+1)/2
		return int(M-N)

	def missingNumber2(self, nums):
		for i in range(nums[-1]+1):
			if nums[i]!=i:
				return i
















































