
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

class Solution(object):

	def reOrderArray(self, arr):
		if arr==None or arr==[]:
			return 
		if len(arr)==1:
			return arr
		start=0
		end=len(arr)-1

		while start<end:

			while arr[start]&0x1==1:
				start+=1
			while arr[end]&0x1==0:
				end-=1

			arr[start], arr[end]=arr[end], arr[start]
		print(start, end, arr)
		arr[start], arr[end]=arr[end], arr[start]

		return arr


S=Solution()
# a=[1, 2, 3, 4, 5]
a=[-1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]
print(S.reOrderArray(a))












































