# n进制转10进制
s="0123456789abcdefghijklmnopqrstuvwxyz"
tmp="11101101"
len1=len(tmp)
res=0
for i in range(len1):
	res+=s.index(tmp[i])*pow(n, len1-i-1) # n代表进制
print(res)