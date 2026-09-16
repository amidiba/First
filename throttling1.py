import time
from functools import wraps
def throttle(seconds=1):
	def outer(func):
		last_time=0
		@wraps(func)
		def wrapper(*a,**k):
			nonlocal last_time
			now=time.time()
			if now- last_time< seconds:
				print("limit reached")
				return None
			last_time=now
			return func(*a,**k)
		return wrapper
	return outer
	
@throttle(0.005)
def h():
			print("hey")
h()
h()
h()
h()
print(time.time())
time.sleep(0.0049)
h()
print(time.time())
			
				