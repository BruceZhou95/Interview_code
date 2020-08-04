
"""
对于原问题12258，我们可以把它分为1和2258,12和258两个子问题。因为我们可以把1看作一个字母，也可以把12看作一个字母（前提是这两个数字在0~25的范围内，不然就没有对应的字母），
基于这个思路就可以用递归解决。注意0与后面一个字符组成0X的形式，不能看作X，只能单个翻译。例如04只能翻译成ae，不能翻译成‘e.
"""

class Solution(object):

	def trans_num_to_str(num):
		if num<0:
			return 0
		if len(str(num)) ==1:
			return 1
		string =str(num)
		f1, f2, g=0, 1, 0
		for i in range(len(string)-2, -1, -1):
			if int(string[i] +string[i+1]) <26:
				g =1
			else:
				g =0
			f2, f1 =f2+g*f1, f2
		return f2
S=Solution()

print(S.trans_num_to_str(9))


























































