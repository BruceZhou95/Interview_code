
"""
单例模式:包含三个要素:1.某个类只有一个实例；2.必须自行创建这个实例；3.必须自行向系统提供这个实例

"""

"""
1.实现__new__方法，然后将类的实例绑定到——instance上
如果cls._instance为None,说明该类没有被实例化过，new一个该类的实例，并返回
如果cls._instance不是None,直接返回_instance
"""

class Singleton1(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, "_instance"):
			orig=super(Singleton1, cls)
			cls._instance=orig.__new__(cls, *args, **kwargs)
		return cls._instance

	# def __new__(cls, *args, *kwargs):
	# 	if not hasattr(cls, "_instance"):
	# 		orig=super（Singleton1, cls）
	# 		cls._instance=orig.__new__(cls, *args, **kwargs)
	# 	return cls._instance

	# def __new__(cls, *args, *kwargs):
	# 	if not hasattr(cls, "_instance"):
	# 		orig=super(Singleton1, cls)
	# 		cls._instance=orig.__new__(cls, *args, **kwargs)
	# 	return cls._instance


class Myclass(Singleton1):
	a=1

one=Myclass()
two=Myclass()

print(id(one))
print(id(two))

"""方法2:共享属性；所谓的单例就是所有引用的(实例、对象)拥有相同的状态(属性)和行为(方法)
因为同一个类拥有相同的方法，现在只需要保证同一个类拥有相同的属性就行
那么只需要保证__dict__属性指向同一个字典(dict)
"""

class Borg(object):
	_state={}
	def __new__(cls, *args, **kwargs):
		ob=super(Borg, cls).__new__(cls, *args, **kwargs)
		ob.__dict__=cls._state 
		return ob

	_state={}
	def __new__(cls, *args, **kwargs):
		obj=super(Borg, cls).__new__(cls, *args, **kwargs)
		obj.__dict__=cls._state 
		return obj


class MyClass1(Borg):
	a=2

one1=MyClass1()
two2=MyClass1()

print(id(one1) == id(two2)) # False
print(id(one1.__dict__)==id(two2.__dict__)) # True






class A(object):

	def __init__(self, a):
		self.num=2
		rgt=2
		rgt+=a

	def run(self):
		return self.num, rgt

ar=A(2)
a1, a2=ar.run()
print(a1, a2)




































