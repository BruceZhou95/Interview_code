
'''
一个整型数组里除两个数字之外，其他数字都出现了两次。请写程序找
出这两个只出现一次的数字。要求时间复杂度是o(n),空间复杂度是0(1)。

'''




class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp=0
        # 首先自遍历异或操作得出一个值
        for i in nums:
            tmp^=i # 最后一个数字是7
            print(tmp, "**")
        #求这个值右边第一个1的值
        num=1  
        while not(tmp&num):
            num=num+1

        print(num, "@@", bin(num))
        result1=0
        result2=0
        #根据这个值对两个数组进行划分
        for i in nums:
            if (i&num): # 二进制中右边第num个不是1的数字
                result1^=i #自身求异或去掉重复元素
            else:       # 二进制中右边第num个是1的数字
                result2^=i # 
        return [result1,result2]

    def singleNumbers1(self, nums):

        if not nums or len(nums)<=0:
            return 0
        tmp=0
        for i in nums:
            tmp^=i 

        num=1
        while not num&tmp:
            num+=1

        result1=0
        result2=0
        for i in nums:
            if i&num: # 
                result1^=i 
            else:
                result2^=i
        return [result1, result2]

s=Solution()
print(s.singleNumbers1([2,4,3,6,3,2,5,5]))








































