def apply_all(*dicorts):
	def wrapper(func):
		for d in reversed(dicorts):
			func=d(func)
		return func
	return wrapper
def f(func):
	def wrapper(x, y):
		print("i'm f")
		return func(x,y)
	return wrapper

def h(func):
	def wrapper(x , y):
		print("i'm h")
		return func(x,y)
	return wrapper
def j(func):
	def wrapper(x,y):
		print("i'm j")
		return func(x,y)
	return wrapper
@apply_all(f, h, j)
def k(x, y):
	return x + y

k(7,8)

