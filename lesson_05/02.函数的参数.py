#定义
def fn(a):
	print('a = ', a)	

def fn1(a, b, c):
	print('a = ', a)	
	print('b = ', b)	
	print('c = ', c)	

fn(1)

# 关键字参数
fn1(a=10, c=20, b=1)

# 关键字参数与位置参数混合

# 实参类型可以为任意类型
fn1('h', 2, 'abc')

# 实参可以传递函数
fn(fn1)


