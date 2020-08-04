'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''
from functools import cmp_to_key


class Solution:
	def PrintMinNumber(self, numbers):
		if numbers==None or len(numbers)<=0:
			return ""

		strlist=[]
		for i in numbers:
			strlist.append(str(i))
		key=cmp_to_key(lambda x, y:int(x+y)-int(y+x))
		strlist.sort(key=key)
		print(strlist)
		return "".join(strlist)

	# def PrintMinNumber1(self, numbers):
	# 	if numbers==None or len(numbers)<=0:
	# 		return ""
	# 	strlist=[str(i) for i in numbers]
	# 	for i in range(len(strlist)-1):
	# 		for j in range(len(strlist)-i-1):
	# 			if strlist[i]>strlist[i+1]:
	# 				strlist[i], strlist[i+1]=strlist[i+1], strlist[i]

	def PrintMinNumber1(self, numbers):
		if numbers==None or len(numbers)<=0:
			return ""

		strlist=[str(i) for i in numbers]
		key=cmp_to_key(lambda x, y:int(x+y)-int(y+x))
		strlist.sort(key=key)
		return "".join(strlist)


S=Solution()
numbers=[322,321,13]
print(S.PrintMinNumber1(numbers))
# print(S.PrintMinNumber1(numbers))
# print(numbers)



a={"b":2, "a":3, "c":8, "d":1}

b=sorted(a.items(), key=lambda x:x[1], reverse=True)

for c, n in b:
	print(c, n)

print(b)


			

































