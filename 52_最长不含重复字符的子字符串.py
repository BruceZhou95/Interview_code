'''
从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。假设字符串中只包含'a'~'z的字符。例如，在字
符串"arabcacfr"中，最长的不含重复字符的子字符串是"acfr",长度为4。
'''
class Solution:
	def lengthOfLongestSubstring(self, s):
		if len(s) <= 1:
			return len(s)
		head, tail = 0, 0
		maxLen = 1
		while tail+1 < len(s):
			tail += 1  # 往窗口内添加元素
			if s[tail] not in s[head: tail]:  # 窗口内没有重复的字符，实时更新窗口最大长度
				maxLen = max(maxLen, tail - head + 1)
			else:  # 窗口内有重复字符，移动head直至窗口内不再含重复的元素
				while s[tail] in s[head: tail]:
					head += 1
		return maxLen

	def lengthOfLongestSubdtring1(self, s):
		if len(s)<=1:
			return len(s)
		head, tail=0, 0
		maxLen=1
		while tail+1<len(s):
			tail+=1 # 王窗口内添加元素
			if s[tail] not in s[head:tail]:# 如果窗口内没有重复的字符，实时更新窗口的元素
				maxLen=max(maxLen, tail-head+1)
			else:  # 窗口内有重复字符，移动head直至窗口内不再含重复的元素
				while s[tail] in s[head:tail]:
					head+=1 # 当有重复的数字时首指针会一直相加
		return maxLen

	def lengthOfLongestSubdtring2(self, s):
		if len(s)<=1:
			return len(s)
		head, tail=0, 0 # 双指针
		maxLen=1
		while tail+1<len(s):
			tail+=1
			if s[tail] not in s[head:tail]:
				maxLen=max(maxLen, tail-head+1)
			else:
				while s[tail] in s[head:tail]:
					head+=1
		return maxLen


s=Solution()
print(s.lengthOfLongestSubdtring2("yyabcdabjcabceg")) # cdabj



















































