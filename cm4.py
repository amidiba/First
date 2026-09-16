from contextlib import contextmanager
import time
@contextmanager
def g():
	start=time.time()
	print("started")

	try:
		yield 67
	except Exception as e:
		print(f"erorr: ({e}) occurred")
		raise
	finally:
		print(g)
		print("end")
		print(f"took: {time.time()-start:.4F} seconds")
with g() as g:
	print(1/0)
	
