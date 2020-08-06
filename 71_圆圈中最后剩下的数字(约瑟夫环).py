'''
0, 1, 2, n-1这n个数字排成一个圆环, 从数字0开始每次从这个圆圈里删除第m个数字
求这个圆圈中最后剩下的一个数字
'''

class Solution(object):

	def LastRemain(self, n, m): # 0~n-1
		if n<1 or m<1:
			return None 

		last=0
		for i in range(2, n+1):
			last=(last+m)%i

		return last 

s=Solution()
print(s.LastRemain(5, 1))
















































