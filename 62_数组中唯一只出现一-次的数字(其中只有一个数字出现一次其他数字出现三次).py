'''
在一个数组中除一个数字只出现一次之外，其他数字都出现了三次.请找出那个只出现一次的数字。
'''

class Solution(object):

	def FindNumberAppearingOnce(self, numbers):
		if not numbers or len(numbers)<=0:
			return None 

		BitSum=[0]*32
		for i in range(len(numbers)):
			bitMask=1
			for j in range(31, -1, -1):
				bit=numbers[i]&bitMask
				if bit!=0:
					BitSum[j]+=1
				bitMask=bitMask<<1
		res=0
		for i in range(32):
			res<<=1
			res+=BitSum[i]%3
		return res

	def FindNumberAppearingOnce1(self, numbers):
		if not numbers or len(numbers)<=0:
			return None 

		bitSum=[0]*32
		for i in range(len(numbers)):
			bitMask=1
			for j in range(31, -1, -1):
				bit=numbers[i]&bitMask
				if bit!=0:
					bitSum[j]+=1
				bitMask<<=1
		res=0
		for i in range(32):
			res<<=1
			res+=bitSum[i]%3 

		return res 


s=Solution()
print(s.FindNumberAppearingOnce([-209, 3467, -209, -209]))
print(s.FindNumberAppearingOnce1([1024, -1025, 1024, -1025, 1024, -1025, 1023]))


















































