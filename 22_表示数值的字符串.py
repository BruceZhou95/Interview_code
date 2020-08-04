'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''

# Python trick

def isNumeric2(s):
	try:
		float(s)
		if s[:2]!="-+" and s[:2]!="+-":
			return True 
		else:
			return False 
	except:
		return False 

def isNumseric(s):
	try:
		float(s)
		if s[:2]!="+-" and s[:2]!="-+":
			return True
		else:
			return False 
	except:
		return False


print(isNumseric("13.e14")) 

class Solution(object):

	def isNumseric(self, s):
		if s==None or len(s)<=0:
			return False 
		aList=[w.lower() for w in s]
		if "e" in aList:
			indexE=aList.index("e")
			before=aList[:indexE]
			behand=aList[indexE+1:]
			if "." in behand or len(behand)==0:
				return False
			isbefore=self.scanNum(before)
			isbehand=self.scanNum(behand)
			return isbefore and isbehand
		else:
			isNum=self.scanNum(aList)
			return isNum

	def scanNum(self, aList):
		VaList=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-","e", "."]
		dotNum=0
		for i in range(len(aList)):
			if aList[i] not in VaList:
				return False  
			if aList[i]==".":
				dotNum+=1
			if aList[i] in "+-" and i!=0:
				return False 
		if dotNum>1:
			return False 
		return True

	def isNumeric1(self, s):
		if s==None or len(s)<=0:
			return False 

		List1=[w.lower() for w in s]
		if "e" in List1:
			indexE=List1.index("e")
			before=List1[:indexE]
			behand=List1[indexE+1:]
			if "." in behand or len(behand)<=0:
				return False 
			isbefore=self.scanNums(before)
			isbehand=self.scanNums(behand)
			return isbefore and isbehand
		else:
			isNum=self.scanNums(aList)
			return isNum

	def scanNums(self, List1):
		dotNum=0
		VaList=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "e", "e"]

		for i in range(len(List1)):
			if List1[i] not in VaList:
				return False
			if List1[i]==".":
				dotNum+=1
			if List1[i] in "+-" and i!=0:
				return False
		if dotNum>1:
			return False
		return True

	# 第二种方法
	def isNum2(self, s):
		if s==None or len(s)<=0:
			return False 

		# 判断是否有e
		hasE=False 
		# 判断是否有小数
		isDecimal=False
		# 判断是否有+-符号
		hasSign=False 

		for i in range(len(s)):
			# e不能重复且不能是最后一个
			if s[i]=="e" or s[i]=="E":
				if hasE or i==len(s)-1:
					return False 
				hasE=True
			# 小数点不能重复出现或者和e共现
			elif s[i]==".":
				if hasE or isDecimal:
					return False
				isDecimal=True
			elif s[i]=="-" or s[i]=="+":
				# 重复出现符号时，必须跟在e后面
				if hasSign and s[i-1]!=e and s[i-1]!="E":
					return False
				# 重复出现符号时，必须跟在e后面
				if not hasSign and i>0 and s[i-1]!="e" and s[i-1]!="E":
					return False
				hasSign=True 
			elif s[i]<"0" or s[i]>"9":
				return False
		return True

	def isNum21(self, s):

		# 判断是否有E
		hasE=False

		# 判断是否有小数点
		hasDecimal=False

		# 判断是否有符号
		hasSign=False

		for i in range(len(s)):
			# 如果有e不能重复出现，切不能是最后一个
			if s[i]=="E" or s[i]=="e":
				if hasE or i==len(s)-1:
					return False
				hasE=True

			elif s[i]==".":
				if hasE or hasDecimal:
					return False 
				hasDecimal=True
			elif s[i]=="+" or s[i]=="-":
				if hasSign and s[i-1]!="e" and s[i-1]!="E":
					return False 
				if not hasSign and i>0 and s[i-1]!="e" and s[i-1]!="E":
					return False 
				hasSign=True
			elif s[i]<"0" or s[i]>"9":
				return False
		return True 




S=Solution()
# print(S.isNumeric1("e.14"))
print(S.isNum2("2e14"))






























