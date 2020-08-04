
'''
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student."，则输出"student. a am I"。
'''

class SoLution(object):

	def ReveseStr(self, s):
		if s==None:
			return None 
		if s=="" or len(s)==1:
			return s 
		s=s[::-1]

		liS=s.split()
		for i in range(len(liS)):
			liS[i]=liS[i][::-1]

		return " ".join(liS)

s=SoLution()

print(s.ReveseStr("I am a student."))




























































