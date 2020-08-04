# 将数组每个空格替换成%20


def replaceSpace(str1):
	a=str1.replace(" ", "%20")
	return a 

a="I am not happy"

# print(replaceSpace(a))


class Solution(object):

	def replaceSpace(self, str1):
	 	if(str1==None or len(str1)<=0):
	 		return False 

	 	count=0
	 	for i in range(len(a)):
	 		if (str1[i]==" "):
	 			count+=1

	 	newstr=str1+2*count

	 	start=len(a)-1
	 	end=len(newstr)-1

	 	while (start<=end):
	 		if(start==" "):
	 			pass

	 #  新建一个list如果是空格就append("%20") 如果不是就append
	def replaceSpace1(self, str1):
	 	if(str1==None or len(str1)<=0):
	 		return False 

	 	string=list(str1)
	 	stringRepace=[]

	 	for i in str1:
	 		if(i==" "):
	 			stringRepace.append("%20")
	 		else:
	 			stringRepace.append(i)

	 	return "".join(stringRepace)

	# 创建新的字符串进行替换
	def replaceSapce2(self, str1):
		if(str !=type(str1) or str1==None or len(str1)<=0):
			return False 

		str2=""
		for i in str1:
			if(i==" "):
				str2+="%20"
			else:
				str2+=i
		return i 

	# 书中给的解题思路的算法
	def repalceSpace3(self, str1):
		if not isinstance(str1, str) or len(str1)==0 or str1==None:
			return False 

		spaceNum=0
		for i in str1:
			if i==" ":
				spaceNum+=1

		newstrLen=len(str1)+spaceNum*2
		newstr=[None]*newstrLen

		Oriindex, Newindex=len(str1)-1, newstrLen-1

		while (Oriindex>=0 and Newindex>=Oriindex):
			if(str1[Oriindex]==" "):
				newstr[Newindex-2:Newindex+1]=['%', '2', '0']
				Oriindex-=1
				Newindex-=3
			else:
				newstr[Newindex]=str1[Oriindex]
				Newindex-=1
				Oriindex-=1

		return ''.join(newstr)
d=Solution()

print(d.repalceSpace3(a))

# 对两个有序的列表进行排序
def sortDouble(list1, list2):


	len1=len(list1)
	len2=len(list2)

	list3=[None]*(len2+len1)
	len3=len(list3)

	index1=len1-1
	index2=len2-1
	index3=len3-1

	while index1>=0 and index3>=0 and index2>=0:
		if(list1[index1]>=list2[index2]):
			list3[index3]=list1[index1]
			index1-=1
			index3-=1
		else:
			list3[index3]=list2[index2]
			index2-=1
			index3-=1

	print(list3)
	print(index1, index2, index3)
	if(index1>=0):
		list3[:index3+1]=list1[:index1+1]
		print(list3)
	if(index2>=0) :
		list3[:index3+1]=list2[:index2+1]
		

	return list3


list1=[2,3,4,5, 6, 9, 11, 45]
list2=[4, 7, 21, 45]

print(sortDouble(list1, list2))









































