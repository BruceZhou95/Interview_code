
import time


def feibon(n):
	a, b=0, 1
	for i in range(n):
		a, b=b, a+b

	return a 
tim1=time.time()
print(feibon(1000))
tim2=time.time()

print(tim2-tim1)

print("-"*70)

def feibo2(n):

	a, b=0, 1
	while n:
		a, b=b, a+b
		n-=1
		yield a

for i in feibo2(6):
	print(i)

print("-"*70)

def feibo3(n):
	if n==0:
		return 0
	if n==1:
		return 1
	return feibo3(n-1)+feibo3(n-2)

print(feibo3(10))


import numpy as np 

# 使用矩阵计算斐波那契数列
def Fibonacci_Matrix_tool(n):
    Matrix = np.matrix("1 1;1 0", dtype='int64')
    # 返回是matrix类型
    return np.linalg.matrix_power(Matrix, n)

def Fibonacci_Matrix(n):
    result_list = []
    for i in range(0, n):
        result_list.append(np.array(Fibonacci_Matrix_tool(i))[0][0])
    return result_list

tim1=time.time()
print(Fibonacci_Matrix(50))
tim2=time.time()

print(tim2-tim1)































