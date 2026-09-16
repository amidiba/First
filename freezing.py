def d(func):
	excuted=False
	def wrapper(*a,**k):
		nonlocal excuted
		if excuted:
			print("already done")
			return None
		excuted=True
		return func(*a,**k)
	return wrapper
@d
def x(*a):
	print("x")
x(2)
x(3)
@d
def g():
	print("g")
g()
g()
g()
