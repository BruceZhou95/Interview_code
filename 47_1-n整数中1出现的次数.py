'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
1~13中包含1的数字有1、10、11、12、13因此共出现6次。
'''

class Solution(object):
	def NumberOf1Between1AndN_solution(self, n):
		ones, m=0, 1 
		while m<=n:
			ones+=(n//m+8)//10*m+(n//m%10==1)*(n%m+1)
			m *= 10
		return ones


s = Solution()
import time
start=time.time()
# print(s.NumberOf1Between1AndN_Solution(pow(2, 31)))
print(s.NumberOf1Between1AndN_solution(1300000000))
end=time.time()
print(end-start)










































'''
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
1~13中包含1的数字有1、10、11、12、13因此共出现6次。
'''
