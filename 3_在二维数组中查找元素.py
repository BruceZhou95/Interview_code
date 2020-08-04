# _*_conding:utf-8 _*_

array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]


class Solution(object):
	# array 二维数组列表
	def  find(self, array, target):
		# 判断数组是否为空
		if(array==[]):
			return False

		rownum=len(array)
		colnum=len(array[0])

		if type(target)==float and type(array[0][0]==int):
			if int(target)==target:
				return False 

		elif type(target)==int and type(array[0][0])==float:
			target=float(int)

		else type(target) != type(array[0][0]):
			return False 

		i=colnum-1
		j=0
		while i>=0 and j<rownum:
			if array[j][i]<target:
				j+=1
			elif array[j][i]>target:
				i-=1
			else:
				return True 

		return False

	# 扩展，输出数组中target的个数
	def searchMatrix(self, matrix, target):
		if matrix==None or len(matrix)==0:
			return 0 
		rows=len(matrix)
		cols=len(matrix[0])

		row, col=0, cols-1
		count=0
		while row<=rows-1 and col>=0:
			if(matrix[row][col]>target):
				col-=1
			elif matrix[row][col]<target:
				row+=1
			else:
				count+=1
				col-=1
		return count

	def find2(self, matrix, target):
		if(matrix==None or len(matrix==0)):
			return False 

		rows=len(matrix)
		cols=len(matrix[0])

		if type(target)==float and type(matrix[0][0])==int:
			if(int(target)==target):
				return False 

		elif(type(target)==int) and type(matrix[0][0]=float):
			target=float(int)

		elif type(target)!=type(matrix[0][0]):
			return False 

		i=0 
		j=cols-1

		while i<rows and j>0:
			if(matrix[i][j]<key):
				i+=1
			elif matrix[i][j]>key:
				j-=1
			else:
				return True
		return False 

	def countFind(self, matrix, target):
		if(matrix==None and len(matrix)==0):
			return False 

		cols=len(matrix[0])
		rows=len(matrix)

		i, j=0, cols-1
		while i<rows and j>0:
			if matrix[i][j]>key:
				j-=1

			elif matrix[i][j]<key:
				i+=1

			else:
				count+=1
				j-=1
		return count


	def find3(self, matrix, target):

		if(matrix==None or len(matrix)==0):
			return False 

		if(type(target)==float and type(matrix)==int):
			if(int(target)==target):
				return False 

		if(type(target)==int and type(matrix)==float):
			target=float(int)

		if (type(target)!=type(matrix)):
			return False

		rows=len(matrix)
		cols=len(matrix[0])

		j=0
		i=rows-1
		while i>0 and j<cols:
			if(matrix[i][j]>key):
				i-=1
			elif (matrix[i][j]<key):
				j+=1
			else:
				return True
		return False 


	def countFind3(self, matrix, target):
		if(matrix==None or len(matrix)==0):
			return False

		count=0
		rows=len(matrix)
		cols=len(matrix[0])

		i=rows-1
		j=0

		while(i>0 and j<cols):
			if(matrix[i][j]>key):
				i-=1
			elif(matrix[i][j]<key):
				j+=1
			else:
				count+=1
				i-=1
		return False 


	
	# 判断非法输入

# def ArrayFind(arr, key):

# 	if(arr==[]):
# 		return

# 	rownum=len(arr)
# 	colnum=len(arr[0])

# 	while rownum>=0 and colnum>=0:
# 		i, j=0, colnum
# 		if arr[0][colnum]>key:
# 			colnum-=1

# 		if arr[0][colnum]==key:
# 			return True 

# 		if arr[0][colnum]<key:
# 			rownum+=1




