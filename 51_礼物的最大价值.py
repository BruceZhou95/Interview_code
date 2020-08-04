"""
在一个 m*n 的棋盘中的每一个格都放一个礼物，每个礼物都有一定的价值（价值大于0）.
你可以从棋盘的左上角开始拿各种里的礼物，并每次向右或者向下移动一格，
直到到达棋盘的右下角。给定一个棋盘及上面个的礼物，请计算你最多能拿走多少价值的
礼物？
"""
class Solution(object):

	def getmaxGift(self, values, rows, cols):
		vars1=[0]*cols # 每次更新一行的数据
		for r in range(rows):
			for c in range(cols):
				left=0
				up = 0
				if r>0:
					up=vars1[c]
				if c>0:
					left=vars1[c-1]
				vars1[c]= max(up,left)+values[r*cols+c]
			print('每一轮vars的变化')
			print(vars1)
		return vars1[-1]

	def getMaxGift(self, arr, rows, cols):
		vars1=[0]*cols
		for r in range(rows):
			for c in range(cols):
				left=0
				up=0
				if r>0:
					up=vars1[c]
				if c>0:
					left=vars1[c-1]
				vars1[c]=max(up, left)+arr[r*cols+c]
		return vars1[-1]

	def getMaxGift1(self, arr, rows, cols):
		vars1=[0]*cols
		for r in range(rows):
			for c in range(cols):
				left=0
				up=0
				if r>0:
					up=vars1[c]
				if c>0:
					left=vars1[c-1]
				vars1[c]=max(up, left)+arr[r*cols+c]
		return vars1[-1]

	def getMaxGift2(self, arr, rows, cols):
		vars1=[0]*cols
		for r in range(rows):
			for c in range(cols):
				left=0
				up=0
				if r>0:
					up=vars1[c]
				if c>0:
					left=vars1[c-1]
				vars1[c]=max(up, left)+arr[r*cols+c]

		return vars1[-1]

	def getMaxGift3(self, arr, rows, cols):
		vars1=[0]*cols
		for r in range(rows):
			for c in range(cols):
				left=0
				up=0
				if r>0:
					up=vars1[c]
				if c>0:
					left=vars1[c-1]
				vars1[c]=max(left, up)+arr[r*cols+c]
		return vars1[-1]

	def getMaxGift4(self, arr, rows, cols):
		vars1=[0]*cols
		for r in range(rows):
			for c in range(cols):
				left=0
				up=0
				if r>0:
					up=vars1[c]
				if c>0:
					left=vars1[c-1]
				vars1[c]=max(left, up)+arr[r*cols+c]
		return vars1[-1]

	def getMaxGift5(self, arr, rows, cols):
		vars1=[0]*cols
		for r in range(rows):
			for c in range(cols):
				left=0
				up=0
				if r>0:
					up=vars1[c]
				if c>0:
					left=vars1[c-1]

				vars1[c]=max(left, up)+arr[r*cols+c]

		return vars1[-1]



s=Solution()
values=[1,10,3,8,12,2,9,6,5,7,4,11,3,7,16,5]
print(s.getMaxGift5(values,4,4))





















































