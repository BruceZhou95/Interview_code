'''
输入一个整型数组,数组里有整数也有负数。
数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array == None or len(array) <= 0:
            return 0

        nCurSum = 0
        nGreatestSum = array[0]
        for i in range(len(array)):
            if nCurSum <= 0:
                nCurSum = array[i]
            else:
                nCurSum += array[i]

            if nCurSum > nGreatestSum:
                nGreatestSum = nCurSum

        return nGreatestSum
    # 动态规划解决问题
    def FindGreatestSumOfSubArray2(self, array):
        if array == None or len(array) <= 0:
            return 0
        aList = [0]*len(array)
        for i in range(len(array)):
            if i == 0 or aList[i-1] <= 0:
                aList[i] = array[i]
            else:
                aList[i] = aList[i-1] + array[i]
        return max(aList)



alist = [1, -2, 3, 10, -4, 7, 2, -5]
s = Solution()
print(s.FindGreatestSumOfSubArray2(alist))



# 方法1
def M(arr):
    tmp=0
    maxValue=0

    for i in range(len(arr)):
        tmp=arr[i]
        for j in range(i+1, len(arr)):
            tmp+=arr[j]
            if tmp>maxValue:
                maxValue=tmp

    return maxValue   # 返回值最小为0 [-2, -3, -5, -1, -4]

# 方法2
def M2(arr):
    tmp=0
    maxValue=0
    for i in range(len(arr)):
        tmp+=arr[i]
        if tmp<0:
            tmp=0
        if tmp>maxValue:
            maxValue=tmp

    return maxValue # 返回值最小为0 [-2, -3, -5, -1, -4]

# 方法3
def M3(arr):
    dp=num[:]
    res=num[0]
    for i in range(1, len(arr)):
        dp[i]=max[dp[i], dp[i]+dp[i-1]]
        res=max(res, dp[i])

    return res # 返回连续数组的最大和

# 方法4
def M4(arr):
    max_, sum_=arr[0], arr[0]

    for n in range(1, len(arr)):
        sum_=sum_+arr[n] if sum_>=0 else arr[n]
        max_=sum_ if sum_>max_ else max_

    return max_ # 返回连续数组的最大和







































