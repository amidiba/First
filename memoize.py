from functools import wraps
def d(func):
	cache={}
	@wraps(func)
	def wrapper(*args):
		if args in cache:
			print("from cache")
			print(cache.items())
			return cache[args]
		result=func(*args)
		cache[args]=result
		return result
	return wrapper
@d
def k(x):
	if x>2:
		return x * x
	else:
		return x + x
k(3)
k(3)
print(k(3))