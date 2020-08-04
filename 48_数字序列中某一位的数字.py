import time

def fun():
	s=""
	n=0
	a=200000
	while True:
		if len(s)>a:
			print(s[a])
			break
		s+=str(n)
		n+=1
start=time.time()
fun()
end=time.time()
print(end-start)



def print_num(n):
    length = 0
    for i in range(n):
        length += len(str(i))
        if length >= n:
            return str(i)[length - n]


def nstNum(n):
    mystr = ""
    for i in range(n+1):
        mystr += (str(i))
    return list(mystr)[n-1]

start=time.time()
print(nstNum(200000))
end=time.time()
print(end-start)


"""

题目:数字以0123456789101112131415…的格式序列化到一个字符序列中
在这个序列中，第5位（从O开始计数）是5，第19位位是4，等等。请写一个函数，求任意第n位对应的数字。
"""

def digiAtIndex(n):
	digit, start, count = 1, 1, 9
	while n > count: # 1.
		n -= count
		start *= 10 # 位数的开始数比如2位数开始数为10
		digit += 1 #位数
		count = 9 * start * digit # 经过了多少位
	num = start + (n - 1) // digit # 2.
	print(num)
	return int(str(num)[(n - 1) % digit]) # 3.

def digiAtIndex1(n):
	digit, start, count=1, 1, 9
	while n>count:
		n-=count 
		start*=10
		digit+=1
		count=9*start*digit
	num=start+(n-1) // digit
	return int(str(num)[n-1]%digit)

print(digiAtIndex(10000))


def digitAtIndex2(n):
	digit, start, count=1, 1, 9
	while n>count:
		n-=count
		digit+=1 
		start*=10 
		count=9*start*digit

	num=start+(n-1)//digit

	return int(str(num)[n-1]%digit)











def Wine(n):
	count=0 # 记录喝了多少就

	while n>=3:
		n-=3
		n+=1
		count+=3
		if  n<3:
			count+=n
	return count


print(Wine(9))































