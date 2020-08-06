
"""
给定一个数组A[0, 1, …, n-1]，请构建一个数组 B[0, 1,…, n-1]，其
中B中的元素B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]x…×A[n-1]。不能使用除法。

B[i]=C[i]*D[i]

C[i]=A[0]×A[1]×…×A[i-1]
D[i]=A[i+1]xA[i+1]…×A[n-1]

C[i]=C[i-1]*A[i-1]
D[i]=D[i+1]*A[i+1]


"""


class Solution(object):

	def multiply(self, A):
		if not A or len(A)<=0:
			return 

		length=len(A)
		aList=[1]*length
		for i in range(1, length):
			aList[i]=aList[i-1]*A[i-1] # C[i]

		temp=1
		for i in range(length-2, -1, -1):
			temp=temp*A[i+1] # D[i]
			aList[i] *= temp 
		return aList

	def mutiply1(self, A):
		if not A or len(A)<=0:
			return

		length=len(A)
		aList=[1]*length
		for i in range(1, length):
			aList[i]=aList[i-1]*A[i-1]

		temp=1 
		for i in range(length-2, -1, -1):
			temp*=A[i+1]
			aList[i]*=temp

		return aList

s=Solution()
a=[3, 6, 7, 2, 1, 4]
print(s.multiply(a))
print(s.mutiply1(a))




























































