# 输入一个长度为n的数组，输出数组中重复的数字

a=[2, 3,4,6, 3,2,-5, 4, 5, -3, -5]

def find(a):
	min_a=min(a)
	max_a=max(a)

	num_new=[0]*(max_a-min_a+1)

	for i in a:
		num_new[i-min_a]+=1

	for ind, i in enumerate(num_new):
		if(i>1):
			print(ind+min_a)


# 使用集合
def find2(a):
	if (len(a)==1):
		return
	result=set()
	for i in range(len(a)):
		for j in range(i+1, len(a)):
			if(a[i]==a[j]):
				result.add(a[i])

	return result


def find3(a):
	if(len(a)<=1):
		return 
	for i in range(len(a)):
		pass

class Solution:
	def duplicate(self, numbers, duplication):
		if numbers==None or (len(numbers)<=0):
			return False 
		for i in numbers:
			if(i<0 or i>len(numbers)-1):
				return False 
		for i in range(len(numbers)):
			if(numbers[i]!=i):
				if numbers[i]==numbers[numbers[i]]:
					duplication[0]=numbers[i]
					return True
				else:
					index=numbers[i]
					numbers[i], numbers[index]=numbers[index], numbers[i]

	def duplicate1(self, numbers, duplication):
		if(numbers==None or len(numbers)<2):
			return False 
		for i in numbers:
			if(numbers<0 or numbers>len(n)-1):
				return False 
		for i in range(len(numbers)):
			if(numbers[i]!=i):
				if(numbers[i]==numbers[numbers[i]]):
					duplication[0]=numbers[i]
					return True
				else:
					index=numbers[i]
					numbers[i], numbers[index]=numbers[index], numbers[i]

	def duplicate2(self, numbers, duplication):
		if(numbers==None or len(numbers)<1):
			return False

		for i in numbers:
			if (i>len(numbers)-1 or i<0):
				return False 

		for i in range(len(numbers)):
			while (numbers[i]!=i):
				if(numbers[i]==numbers[numbers[i]]):
					duplication[0]=numbers[i]
					return True
				else:
					index=numbers[i]
					numbers[i], numbers[index]=numbers[index], numbers[i]

		def duplicate3(self, numbers, duplication):
			if (numbers==None or len(numbers)<1):
				return False 
			for i in numbers:
				if(i<0 or i >len(numbers)-1):
					return False 
			for i in range(len(numbers)):
				while numbers[i]!=i:
					if(numbers[i]==numbers[numbers[i]]):
						duplication[0]=numbers[i]
						return True
					else:
						index=numbers[i]
						numbers[index], numbers[i]=numbers[i], numbers[index]


print(find2([3]))


# 不修改原数组
tmp=0
def duplicate(numbers):
	global tmp
	if(numbers==None or len(numbers)<0):
		return False 
	for i in numbers:
		if (i<1 or i>=len(numbers)):
			return False
	copy_=[0]*len(numbers)
	for i in range(len(numbers)):
		while i!=0:
			if copy_[numbers[i]]!=0:
				tmp=numbers[i]
				return True
			copy_[numbers[i]]=numbers[i]

print(duplicate([2,3,5,4,3,2,6,7]), tmp)


# 不修改原数组，但是，判断数字在数组中出现的次数

class Solution(object):

	def duplicate(self, numbers):
		if(numbers==None or len(numbers)<=0):
			return False 
		for i in numbers:
			if (i<1 or i>=len(numbers)):
				return False 
		length=len(numbers)
		start, end=1, length-1
		while(end>=start):
			middle=((end-start)>>1)+start 
			count=countRange(numbers, length, start, middle)
			if(end==start):
				if count>1:
					return start 
				else:
					break 
			if(count>(middle-start+1)):
				end=middle 
			else:
				start=middle+1
		return False 

		def countRange(self, numbers, length, start, end):
			if(numbers==None):
				return False
			count=0
			for i in range(length):
				if(numbers[i]>=start and numbers[i]<=end):
					count+=1
			return count


	def duplicate1(self, numbers):
		if(numbers==None and len(numbers)<=0):
			return False 
		for i in numbers:
			if(i>=len(numbers) and i<1):
				return False 

		length=len(numbers)
		start, end=1, length-1
		while (end>=start):
			middle=((end-start)>>1)+start 
			count=countRange1(numbers, length, start, end)
			if(end==start):
				if count>1:
					return start 
				else:
					break 
			if(count>(middle-start)+1):
				end=middle
			else:
				start=middle+1
			return False

	def countRange1(self, numbers, length, start, end):
		if numbers==None:
			return False 
		count=0
		for i in range(length):
			if(start>=numbers[i] and end<=numbers[i]):
				count+=1
		return count 


	def duplicate2(self, numbers):
		if(numbers==None or len(numbers)<=0):
			return False 
		length=len(numbers)
		for i in range(length):
			if (i<1 or i>=length):
				return False 
		start, end=0, length-1
		while end>=start:
			middle=((end-start)>>1)+start 
			count=countRange2(numbers, length, start, end)
			if(end==start):
				if(count>1):
					return True # start
				else:
					break 
			if (count>(middle-start)+1):
				end=middle
			else:
				start=middle+1
		return False 

	def countRange2(self, numbers, length, start, end):
		if(numbers==None):
			return False

		count=0
		for i in range(length):
			if(numbers[i]>=start and numbers[i]<=end):
				count+=1
		return count

	def duplicate3(self, numbers):
		if(numbers==None or len(numbers)<=0):
			return False

		length=len(numbers) 
		for i in range(length):
			if(numbers[i]<1 or numbers[i]>length-1):
				return False 

		start, end=1, length-1
		while end>=start:
			middle=((end-start)>>1)+start
			count=countRange3(numbers, length, start, middle)
			if(end==start):
				if(count>1):
					reurn True 
				else:
					break 
			if(count>(middle-start+1)):
				end=middle 
			else:
				start=middle+1

			return False 

	def countRange3(self, numbers, length, start, end):
		if(numbers==None):
			return False 
		count=0
		for i in range(length):
			if (numbers[i]>=start and numbers[i]<=end):
				count+=1
		return count


	def duplicate4(self, numbers):
		if(numbers==None or len(numbers)<=0):
			return False

		length=len(numbers) 
		for i in range(length):
			if(i<1 or i>length-1):
				return False 
		start, end=1, length-1

		while(start<=end):
			middle=((end-start)>>1)+start 
			count=countRange4(numbers, length, start, middle)
			if(start==end):
				if(count>1):
					return start 
				else:
					break 
			if(count>(middle-start)+1):
				end=middle
			else:
				start=middle+1

		return False

	def countRange4(self, numbers, length, start, end):
		if(numbers==None):
			return False
		count=0
		for i in range(length):
			if(start<=numbers[i] and numbers[i]<=end):
				count+=1
		return count 








def duplicate(numbers):

	if(numbers==None or len(numbers)<0):
		return False 
	for i in numbers:
		if (i<1 or i>=len(numbers)):
			return False 
	n=len(numbers)
	left, right=1, n-1
	while left<=right:
		if()




a1=0
def t():
	global a1
	a1+=1

def t2():
	a1+=2

# t2()

print(t(), a1)

































































