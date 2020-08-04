'''
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
'''

# 存储在字典中

class Solution(object):

	def FirstcomeChar(self, s):

		if s==None or s=="":
			return " "

		strList=list(s)
		dic={}
		for i in strList:
			if i not in dic.keys():
				dic[i]=0

			dic[i]+=1
		for i in strList:
			if dic[i]==1:
				return i 

		return " "


	# 定义一个函数，输入两个字符串，从第一个字符串中删除在第二个字符串中出现过的所有字符。
	def deletefromTwo(self, s1, s2):
		if s2=="":
			return s1
		if s2==None:
			return 
		s2=set(s2)

		s1=list(s1)

		for i in s2:
			if i in s1:
				while i in s1:
					s1.pop(s1.index(i))

		return "".join(s1)

	# 删除字符串中所有重复出现的字符
	def deletechongfu1(self,s):
		return set(s)

	def deletechongfu2(self, s):
		res=[]
		for i in s:
			if i not in res:
				res.append(i)
		return "".join(res)



s=Solution()
print(s.deletefromTwo("We are students.", "aeiou"))
	
	


















































