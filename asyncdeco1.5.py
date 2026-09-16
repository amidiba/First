import inspect
import time
from functools import wraps
import asyncio
def de(func):
	
	if inspect.iscoroutinefunction(func):
		@wraps(func)
		async def wrapper(*a,**k):
			await asyncio.sleep(0.1)
			print( "aa")
			
			return asyncio.run(func())
	else:
		def wrapper(*a,**k):
			print("bb")
			return func(*a,**b)
	return wrapper
@de
async def g():
	await asyncio.sleep(0.2)
	print("hh")
asyncio.run(g())