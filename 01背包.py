# 求出最优的所包含的具体重量大小
w=[0 , 2 , 3 , 4 , 5 ]			#商品的重量2、3、4、5
v=[0 , 3 , 4 , 5 , 6 ]		#商品的价值3、4、5、6
bagV=8					        #背包允许的最大承重
dp=[[0]*(bagv+1)]*(len(w))		       #动态规划表
item = [0]*5                 #最优解情况
def findMax(): #动态规划
    for i in range (5):
        for j in range(bagV+1):
            if j < w[i]:
                dp[i][j] = dp[i - 1][j];
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])

def findWhat(i,j): #最优解情况
    if i>=0:
        if dp[i][j] == dp[i-1][j]:
            item[i] = 0
            findWhat(i-1,j)
        elif j - w[i] >= 0 and  dp[i][j] == dp[i - 1][j - w[i]] + v[i]:
            item[i] = 1
            findWhat(i-1,j-w[i])

def print1():
    # for i in range(5):
    #     res = []
    #     for j in range(9):
    #         res.append(dp[i][j])
    #     print(res)
    print(item)

findMax()
findWhat(4,8)
print1()
