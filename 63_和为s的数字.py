
'''
输入一个递增排序的数组和-一个数字s,在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

'''



class Solution:
    # 从左右一起查找
    # 因为当两个数的和一定的时候, 两个数字的间隔越大, 乘积越小
    # 所以直接输出查找到的第一对数即可
    def FindNumbersWithSum(self, array, tsum):
        if array == None or len(array) <= 0 or array[-1] + array[-2] < tsum:
            return []
        start = 0
        end = len(array)-1
        while start < end:
            sum = array[start] + array[end]

            if sum < tsum:
                start += 1
            elif sum > tsum:
                end -= 1
            else:
                return [array[start], array[end]]
        return []

test = [1,2,4,7,11,15]
s = Solution()
print(s.FindNumbersWithSum(test, 15))













































