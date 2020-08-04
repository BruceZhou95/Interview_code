
'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''

class Solution(object):

	def movingCount(self, threshold, rows, cols):
		visited=[False]*(rows*cols)
		count=self.movingCountCore(threshold, rows, cols, 0, 0, visited)
		return count

	def movingCountCore(self, threshold, rows, cols, row, col, visited):
		count=0
		if self.check(threshold, rows, cols, row, col, visited):
			visited[row*cols+col]=True
			count=1+self.movingCountCore(threshold, rows, cols, row-1, col, visited)+self.movingCountCore(threshold, rows, cols, row, col-1, visited)+self.movingCountCore(threshold, rows, cols, row+1, col, visited)+self.movingCountCore(threshold, rows, cols, col+1, visited)
		return count

	def check(self, threshold, rows, cols, row, col, visited):
		if row>=0 and row<rows and col>=0 and col<cols and self.getDigitSum(row)+self.getDigitSum(col)<=threshold and not visited[row*cols+col]:
			return True
		return False

	def getDigitSum(self, number):
		sum=0
		while number:
			sum+=number%10
			number=number//10
		return sum











	def movingCount1(self, threshold, rows, cols):
		visited=[False]*(rows*cols)
		count=self.movingCountCore1(threshold, rows, cols, 0, 0, visited)
		return count 

	def movingCountCore1(self, threshold, rows, cols, row, col, visited):
		count=0
		if self.check1(threshold, rows, cols, row, col, visited):
			visited[row*cols+col]=True
			count=1+self.movingCountCore1(threshold, rows, cols, row-1, col, visited)+self.movingCountCore1(threshold, rows, cols, row, col-1, visited)+self.movingCountCore1(threshold, rows, cols, row+1, col, visited)+self.movingCountCore1(threshold, rows, cols, row, col+1, visited)
		return count

	def check1(self, threshold, rows, cols, row, col, visited):
		if row>=0 and row<rows and col>=0 and col<cols and self.getDigitSum1(row)+self.getDigitSum1(col)<=threshold and not visited[row*cols+col]:
			return True
		return False 

	def getDigitSum1(self, number):
		sum=0
		while number:
			sum+=number%10
			number//=10
		return sum



	def movingCount2(self, threshold, rows, cols):
		visited=[False]*(rows*cols)
		count=self.movingCountCore2(threshold, rows, cols, 0, 0, visited)
		return count

	def movingCountCore2(self, threshold, rows, cols, row, col, visited):
		count=0
		if self.check2(threshold, rows, cols, row, col, visited):
			visited[row*cols+col]=True
			count= 1 +self.movingCountCore2(threshold, rows, cols, row, col-1, visited)+self.movingCountCore2(threshold, rows, cols, row-1, col, visited)+self.movingCountCore2(threshold, rows, cols, row+1,col, visited)+self.movingCountCore2(threshold, rows, cols, row, col+1, visited)
		return count

	def check2(self, rows, cols, row, col, visited):
		if row>=0 and row<rows, and col>=0 and col<cols and self.getDigitSum2(row)+self.getDigitSum2(col) and not visited[row*cols+col]:
			return True
		return False

	def getDigitSum2(self, number):
		sum=0
		while number:
			sum+=number%10
			number//=10











































