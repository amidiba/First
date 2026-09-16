class Singleton(type):
	_instances={}
	def __call__(cls, *a, **k):
		if cls not in cls._instances:
			cls._instances[cls] = super().__call__(*a, **k)
		return cls._instances[cls]
class A(metaclass=Singleton):
	pass
a1=A()
a2=A()
print(a1 is a2)
class B(metaclass=Singleton): pass
b1=B()
b2=B()
print(b1 is b2)
